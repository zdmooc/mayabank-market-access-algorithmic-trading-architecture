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

TOPIC_SIGNALS = os.getenv("TOPIC_SIGNALS","strategy.signals")
TOPIC_ORDERS = os.getenv("TOPIC_ORDERS","orders.new")
MAX_NOTIONAL = float(os.getenv("MAX_NOTIONAL","5000"))
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
consumer = kafka_consumer(BOOTSTRAP, TOPIC_SIGNALS, group="risk-engine", auto_offset_reset="latest")

def ensure_tables():
    with pg_conn() as conn, conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS risk_decisions (
          id text PRIMARY KEY,
          signal_id text NOT NULL,
          symbol text NOT NULL,
          side text NOT NULL,
          decision text NOT NULL,
          reason text NOT NULL,
          ts timestamptz NOT NULL
        );
        """)
        conn.commit()

def loop():
    ensure_tables()
    log.info("risk loop signals=%s orders=%s max_notional=%s", TOPIC_SIGNALS, TOPIC_ORDERS, MAX_NOTIONAL)
    while True:
        msg_pack = consumer.poll(timeout_ms=500)
        for _tp, msgs in msg_pack.items():
            for msg in msgs:
                sig = msg.value
                sym = sig["symbol"]
                side = sig["side"]
                price = float(sig.get("price", 100.0))
                qty = 10
                notional = price * qty
                allow = notional <= MAX_NOTIONAL
                decision = "ALLOW" if allow else "REJECT"
                reason = "ok" if allow else f"notional {notional:.2f} > {MAX_NOTIONAL:.2f}"
                rid = str(uuid.uuid4())
                with pg_conn() as conn, conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO risk_decisions (id,signal_id,symbol,side,decision,reason,ts) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (rid, sig["id"], sym, side, decision, reason, utc_now_iso())
                    )
                    conn.commit()

                if allow:
                    order = {
                        "type":"ORDER",
                        "id": str(uuid.uuid4()),
                        "source":"risk-engine",
                        "symbol": sym,
                        "side": side,
                        "qty": qty,
                        "order_type": "MARKET",
                        "ts": utc_now_iso()
                    }
                    producer.send(TOPIC_ORDERS, key=sym, value=order)
                    producer.flush(0.1)

@app.on_event("startup")
def start_bg():
    threading.Thread(target=loop, daemon=True).start()

@app.get("/")
def root():
    return {"service":"risk-engine","topics":{"signals":TOPIC_SIGNALS,"orders":TOPIC_ORDERS},"max_notional":MAX_NOTIONAL}
