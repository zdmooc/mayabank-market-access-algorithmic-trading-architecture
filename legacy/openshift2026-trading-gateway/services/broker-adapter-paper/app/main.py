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
import random

TOPIC_ORDERS = os.getenv("TOPIC_ORDERS","orders.new")
TOPIC_FILLS = os.getenv("TOPIC_FILLS","fills.executed")
TOPIC_ORDER_STATE = os.getenv("TOPIC_ORDER_STATE","orders.state")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
consumer_orders = kafka_consumer(BOOTSTRAP, TOPIC_ORDERS, group="broker-adapter-paper", auto_offset_reset="latest")

def loop():
    log.info("paper broker loop orders=%s fills=%s", TOPIC_ORDERS, TOPIC_FILLS)
    while True:
        msg_pack = consumer_orders.poll(timeout_ms=500)
        for _tp, msgs in msg_pack.items():
            for msg in msgs:
                order = msg.value
                oid = order.get("id")
                sym = order.get("symbol")
                qty = int(order.get("qty", 0))
                if not oid or not sym or qty <= 0:
                    continue

                price = float(order.get("price", 100.0)) + random.uniform(-0.2, 0.2)
                fill_id = str(uuid.uuid4())
                fill = {"type":"FILL","id": fill_id,"order_id": oid,"symbol": sym,"qty": qty,"price": round(price, 4),"ts": utc_now_iso()}
                producer.send(TOPIC_FILLS, key=sym, value=fill)

                state = {"type":"ORDER_STATE","order_id": oid, "state":"FILLED", "ts": utc_now_iso()}
                producer.send(TOPIC_ORDER_STATE, key=sym, value=state)

                producer.flush(0.1)

@app.on_event("startup")
def start_bg():
    threading.Thread(target=loop, daemon=True).start()

@app.get("/")
def root():
    return {"service":"broker-adapter-paper","topics":{"orders":TOPIC_ORDERS,"fills":TOPIC_FILLS,"order_state":TOPIC_ORDER_STATE}}
