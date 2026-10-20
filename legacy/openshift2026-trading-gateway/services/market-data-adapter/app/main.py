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
import random
import threading

TOPIC_TICKS = os.getenv("TOPIC_TICKS","md.ticks")
SYMBOLS = [s.strip() for s in os.getenv("SYMBOLS","AAPL,MSFT,GOOG").split(",") if s.strip()]
TICK_HZ = float(os.getenv("TICK_HZ","5"))
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
prices = {s: 100.0 + random.random()*20 for s in SYMBOLS}

def loop():
    log.info("tick loop start topic=%s symbols=%s hz=%s", TOPIC_TICKS, SYMBOLS, TICK_HZ)
    while True:
        for s in SYMBOLS:
            prices[s] = max(1.0, prices[s] + random.uniform(-0.5, 0.5))
            evt = {"type":"TICK","symbol": s, "price": round(prices[s], 4), "ts": utc_now_iso()}
            producer.send(TOPIC_TICKS, key=s, value=evt)
        producer.flush(0.1)
        time.sleep(max(0.01, 1.0/TICK_HZ))

@app.on_event("startup")
def start_bg():
    threading.Thread(target=loop, daemon=True).start()

@app.get("/")
def root():
    return {"service":"market-data-adapter","topic":TOPIC_TICKS,"symbols":SYMBOLS}
