import os, json, time, uuid, logging
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field
from kafka import KafkaProducer, KafkaConsumer
import psycopg2
import psycopg2.extras

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("svc")

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

def kafka_producer(bootstrap: str):
    return KafkaProducer(
        bootstrap_servers=bootstrap.split(","),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        key_serializer=lambda v: (v.encode("utf-8") if isinstance(v, str) else v),
        acks="all",
        retries=5,
    )

def kafka_consumer(bootstrap: str, topic: str, group: str, auto_offset_reset: str = "latest"):
    return KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap.split(","),
        group_id=group,
        enable_auto_commit=True,
        auto_offset_reset=auto_offset_reset,
        value_deserializer=lambda b: json.loads(b.decode("utf-8")),
    )

def pg_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST","postgres"),
        port=int(os.getenv("POSTGRES_PORT","5432")),
        dbname=os.getenv("POSTGRES_DB","tradingdb"),
        user=os.getenv("POSTGRES_USER","trading"),
        password=os.getenv("POSTGRES_PASSWORD","trading"),
    )

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status":"ok","ts": utc_now_iso()}
import threading

TOPIC_ORDERS = os.getenv("TOPIC_ORDERS","orders.new")
TOPIC_ORDER_STATE = os.getenv("TOPIC_ORDER_STATE","orders.state")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
consumer_state = kafka_consumer(BOOTSTRAP, TOPIC_ORDER_STATE, group="order-manager", auto_offset_reset="latest")

class CreateOrder(BaseModel):
    symbol: str
    side: str = Field(pattern="^(BUY|SELL)$")
    qty: int = Field(gt=0, le=1000000)
    type: str = Field(default="MARKET")

def ensure_tables():
    with pg_conn() as conn, conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
          id text PRIMARY KEY,
          symbol text NOT NULL,
          side text NOT NULL,
          qty int NOT NULL,
          order_type text NOT NULL,
          state text NOT NULL,
          ts_created timestamptz NOT NULL,
          ts_updated timestamptz NOT NULL
        );
        """)
        conn.commit()

def update_loop():
    ensure_tables()
    log.info("order-manager update loop topic=%s", TOPIC_ORDER_STATE)
    while True:
        msg_pack = consumer_state.poll(timeout_ms=500)
        for _tp, msgs in msg_pack.items():
            for msg in msgs:
                evt = msg.value
                oid = evt.get("order_id")
                state = evt.get("state")
                if not oid or not state:
                    continue
                with pg_conn() as conn, conn.cursor() as cur:
                    cur.execute("UPDATE orders SET state=%s, ts_updated=%s WHERE id=%s", (state, utc_now_iso(), oid))
                    conn.commit()

@app.on_event("startup")
def start_bg():
    threading.Thread(target=update_loop, daemon=True).start()

@app.post("/orders")
def create_order(o: CreateOrder):
    ensure_tables()
    oid = str(uuid.uuid4())
    now = utc_now_iso()
    with pg_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO orders (id,symbol,side,qty,order_type,state,ts_created,ts_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (oid, o.symbol, o.side, o.qty, o.type, "NEW", now, now)
        )
        conn.commit()

    evt = {"type":"ORDER","id": oid,"source":"order-manager","symbol": o.symbol,"side": o.side,"qty": o.qty,"order_type": o.type,"ts": now}
    producer.send(TOPIC_ORDERS, key=o.symbol, value=evt)
    producer.flush(0.1)
    return {"id": oid, "state": "NEW"}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    ensure_tables()
    with pg_conn() as conn, conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
        row = cur.fetchone()
        if not row:
            return {"error":"not_found","id": order_id}
        return dict(row)

@app.get("/")
def root():
    return {"service":"order-manager","topics":{"orders":TOPIC_ORDERS,"order_state":TOPIC_ORDER_STATE}}
