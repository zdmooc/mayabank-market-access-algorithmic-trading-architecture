# I11 — Evidence Pack

Status: **IMPLEMENTED / CI_EVIDENCE_PENDING**

Automated scenarios: accepted order, risk reject, partial/full fill, cancel/fill race, stale Market Data, sequence gap, duplicate, reconnect sequence persistence, selective kill and synthetic latency benchmark.

Evidence vocabulary remains strict:
- code exists → IMPLEMENTED;
- green CI → executable CI evidence;
- benchmark numbers → PERFORMANCE_MEASURED_SYNTHETIC only;
- synthetic results never become production latency claims.

Workflow: `.github/workflows/ci.yml`.
