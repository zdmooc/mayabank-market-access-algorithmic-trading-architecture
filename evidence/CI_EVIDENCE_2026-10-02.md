# CI Evidence — 2026-10-02

## Result

**PASS**

- Workflow: Market Access Synthetic CI
- Run: `37043637911`
- Commit: `9d589b7457032fc22c8f9e537f851626979a000d`
- Job: `synthetic-evidence`

## Functional evidence

```text
Ran 10 tests in 0.001s
OK

ORD-1 FILLED 10000 0
ORD-2 REJECTED MAX_QTY
DROP_COPY_EVENTS 5
```

Covered test themes:
- happy path and quantity invariant;
- risk quantity reject;
- notional reject;
- instrument entitlement reject;
- stale Market Data reject;
- cancel/fill race;
- FIX-like gap/duplicate/reconnect;
- replay;
- selective kill;
- overfill rejection.

## Synthetic performance evidence

```json
{
  "sample_count": 5000,
  "unit": "microseconds",
  "p50": 1.012,
  "p95": 1.854,
  "p99": 2.656,
  "p999": 9.336,
  "max": 27.892,
  "mean": 1.122,
  "claim": "PERFORMANCE_MEASURED_SYNTHETIC_ONLY"
}
```

## Truth boundary

This benchmark measures only an in-process deterministic synthetic risk-check function on a GitHub-hosted runner.

It does **not** measure:
- real FIX engine latency;
- TCP/network round trip;
- exchange gateway latency;
- colocation;
- multicast feed handling;
- production hardware/kernel tuning;
- production HFT.
