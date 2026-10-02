# I12 — Interview Answer Key

Use these answers as rehearsal anchors, not as memorized scripts.

1. **Session vs connection** — TCP/TLS is transport; the trading session keeps logical sequence/correlation state across reconnects.
2. **Sequence gap** — stop treating the stream as continuous, request/recover missing messages, then resume from an authoritative sequence state.
3. **Fill crossing Cancel** — Cancel is a request, not a guarantee; the venue may execute before processing it.
4. **Drop Copy** — independent control/reconciliation path for order/execution events.
5. **Pre-trade placement** — as close to execution as required by latency and control ownership, without bypass paths.
6. **Selective kill** — requires reliable active-order indexing by trader/algo/client/venue/instrument/route and auditable cancel outcomes.
7. **Snapshot vs incremental** — snapshot rebuilds complete state; incrementals mutate an already synchronized state.
8. **Stale Market Data** — data whose age/continuity no longer satisfies routing/risk policy.
9. **Why p99** — tail behavior exposes outliers/jitter hidden by averages and often matters operationally.
10. **Clock sync** — needed to reconstruct causality, measure latency and support audit/compliance.
11. **What stays in colo** — venue gateways/native adapters/latency-critical controls/feed handling when measured NFR justify proximity.
12. **What can move cloud** — historical data, analytics, backtesting, observability backends, reporting, CI/CD and other non-critical workloads.
13. **Why not Kafka in hot path by default** — it adds a distributed asynchronous dependency where deterministic synchronous latency may dominate; use it around the hot path when appropriate.
14. **Gateway failover state** — session sequence, message persistence/replay ability, active-order correlation and authoritative route state.
15. **Ambiguous order state** — freeze unsafe actions, recover session, compare main flow/Drop Copy, reconcile, then controlled resume.
16. **Proof before moving workload** — baseline latency/jitter/failure behavior, candidate placement test, compare evidence, then decide.
17. **OMS vs EMS vs SOR** — OMS owns order lifecycle, EMS pilots execution, SOR chooses route/venue.
18. **FIXT vs FIXP** — FIXT separates session/application-version concerns; FIXP is a high-performance session-family concept. No production FIXP claim here.
19. **Avoid overclaiming** — label architecture vs implementation vs synthetic evidence and explicitly state what is not proven.
20. **Questions before target design** — asset classes, venues, protocols, current latency/jitter, session/recovery, Market Data sources, pre-trade ownership, placement, failure model, cloud scope and required evidence.

## 15-minute oral sequence

```text
0–2   mission/context + hot/near/elastic split
2–5   order lifecycle + OMS/EMS/SOR/risk/gateway
5–8   FIX session + sequence/recovery
8–10  Market Data + stale/gap/entitlements
10–12 latency/time/resilience
12–14 hybrid placement
14–15 evidence, limits, questions to client
```

## Positioning sentence

> Architecte Solution senior CIB / Trading, expérimenté sur les systèmes critiques et la transformation d’architecture, avec une spécialisation Market Access / Electronic Trading consolidée par une architecture de référence et un lab synthétique démontrable.

## Boundary sentence

> Je ne me présente pas comme développeur C++ HFT ni comme expert production FIX certifié venue ; mon apport est l’architecture de transformation, les frontières applicatives, la résilience, la performance, l’observabilité et le placement hybride.
