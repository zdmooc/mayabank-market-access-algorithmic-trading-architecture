# I11 — Evidence Pack

Status: **DONE — CI EVIDENCE PASS**

Automated scenarios: accepted order, risk reject, partial/full fill, cancel/fill race, stale Market Data, sequence gap, duplicate, reconnect sequence persistence, selective kill and synthetic latency benchmark.

Evidence vocabulary remains strict:
- code exists → IMPLEMENTED;
- green CI → executable CI evidence;
- benchmark numbers → PERFORMANCE_MEASURED_SYNTHETIC only;
- synthetic results never become production latency claims.

Workflow: `.github/workflows/ci.yml`.


## Observed evidence — 2026-10-02

Run: `37043637911` — **SUCCESS**  
Commit: `9d589b7457032fc22c8f9e537f851626979a000d`

- 10 automated tests passed;
- synthetic demo passed;
- 5,000 risk-control calls measured;
- p50: 1.012 µs;
- p95: 1.854 µs;
- p99: 2.656 µs;
- p99.9: 9.336 µs;
- max: 27.892 µs;
- mean: 1.122 µs.

Boundary: `PERFORMANCE_MEASURED_SYNTHETIC_ONLY`.
