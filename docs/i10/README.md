# I10 — Synthetic Market Access Runtime

Status: **IMPLEMENTED_SYNTHETIC**

Executable path:
```text
Order → state machine → deterministic risk → FIX-like session simulator
      → synthetic venue/fills → Drop Copy → reconciliation evidence
```

Also covers stale Market Data, sequence gaps/duplicates, reconnect state, selective kill and synthetic latency measurement.

Explicitly not implemented: full FIX engine, real venue protocol/connectivity, multicast feed, real colocation, venue certification, real-money trading or production latency proof.

Run:
```bash
python -m pip install -e .
python -m market_access_lab.demo
python -m unittest discover -s tests -v
python evidence/benchmark.py
```
