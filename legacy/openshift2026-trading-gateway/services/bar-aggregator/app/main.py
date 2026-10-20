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

TOPIC_TICKS = os.getenv("TOPIC_TICKS","md.ticks")
TOPIC_BARS = os.getenv("TOPIC_BARS","md.bars")
WINDOW_SECONDS = int(os.getenv("BAR_WINDOW_SECONDS","5"))
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS","redpanda:9092")

producer = kafka_producer(BOOTSTRAP)
consumer = kafka_consumer(BOOTSTRAP, TOPIC_TICKS, group="bar-aggregator", auto_offset_reset="latest")

def ensure_tables():
    with pg_conn() as conn, conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS bars (
          id text PRIMARY KEY,
          symbol text NOT NULL,
          window_seconds int NOT NULL,
          t_start timestamptz NOT NULL,
          t_end timestamptz NOT NULL,
          open numeric NOT NULL,
          high numeric NOT NULL,
          low numeric NOT NULL,
          close numeric NOT NULL,
          ticks int NOT NULL
        );
        """)
        conn.commit()

def aggregate_loop():
    ensure_tables()
    log.info("bar loop start ticks=%s bars=%s window=%ss", TOPIC_TICKS, TOPIC_BARS, WINDOW_SECONDS)
    state = {}
    t0 = time.time()

    def flush(symbol, bar):
        bar_id = str(uuid.uuid4())
        out = {
            "type":"BAR",
            "id": bar_id,
            "symbol": symbol,
            "window_seconds": WINDOW_SECONDS,
            "t_start": bar["t_start"],
            "t_end": bar["t_end"],
            "open": bar["open"],
            "high": bar["high"],
            "low": bar["low"],
            "close": bar["close"],
            "ticks": bar["ticks"],
        }
        producer.send(TOPIC_BARS, key=symbol, value=out)
        producer.flush(0.1)
        with pg_conn() as conn, conn.cursor() as cur:
            cur.execute(
                """INSERT INTO bars (id,symbol,window_seconds,t_start,t_end,open,high,low,close,ticks)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (bar_id, symbol, WINDOW_SECONDS, out["t_start"], out["t_end"], out["open"], out["high"], out["low"], out["close"], out["ticks"])
            )
            conn.commit()

    while True:
        now = time.time()
        if now - t0 >= WINDOW_SECONDS:
            t_end = utc_now_iso()
            for sym, bar in list(state.items()):
                bar["t_end"] = t_end
                flush(sym, bar)
            state = {}
            t0 = now

        msg_pack = consumer.poll(timeout_ms=200)
        for _tp, msgs in msg_pack.items():
            for msg in msgs:
                evt = msg.value
                sym = evt["symbol"]
                price = float(evt["price"])
                if sym not in state:
                    state[sym] = {
                        "t_start": utc_now_iso(),
                        "t_end": utc_now_iso(),
                        "open": price,
                        "high": price,
                        "low": price,
                        "close": price,
                        "ticks": 1
                    }
                else:
                    bar = state[sym]
                    bar["high"] = max(bar["high"], price)
                    bar["low"] = min(bar["low"], price)
                    bar["close"] = price
                    bar["ticks"] += 1

@app.on_event("startup")
def start_bg():
    threading.Thread(target=aggregate_loop, daemon=True).start()

@app.get("/")
def root():
    return {"service":"bar-aggregator","topics":{"ticks":TOPIC_TICKS,"bars":TOPIC_BARS},"window_seconds":WINDOW_SECONDS}
