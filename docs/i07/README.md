# I07 — Colocation / On-Prem / Cloud Placement

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

| Capability | Colo | On-prem | Cloud |
|---|---:|---:|---:|
| venue gateway/native adapter | strong | possible | exceptional/evidence-driven |
| deterministic pre-trade | strong | strong | only with proven NFR |
| low-latency feed handler | strong | possible | workload-dependent |
| OMS/EMS | possible | strong | possible by NFR |
| reference/historical data | possible | strong | strong |
| analytics/backtesting | weak | possible | strong |
| observability backend/CI | weak | strong | strong |

Decision dimensions: latency/jitter, proximity, failure isolation, security, data gravity, operability, cost/egress and DR.

Cloud is selective. Move elastic/analytical workloads first; move order-path components only with measured evidence.
