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
from collections import deque

TOPIC_BARS = os.getenv("TOPIC_BARS","md.bars")
TOPIC_SIGNALS = os.getenv("TOPIC_SIGNALS","strategy.signals")
FAST_MA = int(os.getenv("FAST_MA","3"))
SLOW_MA = int(os.getenv("SLOW_MA","8"))
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
consumer = kafka_consumer(BOOTSTRAP, TOPIC_BARS, group="strategy-runner", auto_offset_reset="latest")

def mean(xs):
    return sum(xs)/len(xs) if xs else 0.0

def loop():
    log.info("strategy loop bars=%s signals=%s fast=%s slow=%s", TOPIC_BARS, TOPIC_SIGNALS, FAST_MA, SLOW_MA)
    closes = {}
    last_state = {}
    while True:
        msg_pack = consumer.poll(timeout_ms=500)
        for _tp, msgs in msg_pack.items():
            for msg in msgs:
                bar = msg.value
                sym = bar["symbol"]
                c = float(bar["close"])
                if sym not in closes:
                    closes[sym] = deque(maxlen=SLOW_MA)
                closes[sym].append(c)
                if len(closes[sym]) < SLOW_MA:
                    continue
                arr = list(closes[sym])
                fast = mean(arr[-FAST_MA:])
                slow = mean(arr)
                state = "ABOVE" if fast > slow else "BELOW"
                prev = last_state.get(sym)
                last_state[sym] = state
                if prev and prev != state:
                    side = "BUY" if state == "ABOVE" else "SELL"
                    signal = {
                        "type":"SIGNAL",
                        "id": str(uuid.uuid4()),
                        "symbol": sym,
                        "side": side,
                        "reason": f"ma_cross fast={FAST_MA} slow={SLOW_MA}",
                        "ts": utc_now_iso(),
                        "price": c
                    }
                    producer.send(TOPIC_SIGNALS, key=sym, value=signal)
                    producer.flush(0.1)

@app.on_event("startup")
def start_bg():
    threading.Thread(target=loop, daemon=True).start()

@app.get("/")
def root():
    return {"service":"strategy-runner","topics":{"bars":TOPIC_BARS,"signals":TOPIC_SIGNALS},"fast_ma":FAST_MA,"slow_ma":SLOW_MA}
