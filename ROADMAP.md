# Roadmap I00 → I12

## Objective

Build a demonstrable reference architecture for a Senior Architect mission covering Market Access, Algorithmic Trading transformation, low-latency performance, rationalisation and hybrid placement across colocation, on-premise and cloud.

## Iterations

| Iteration | Scope | Exit criteria | Status |
|---|---|---|---|
| I00 | Scope, truth model, boundaries | README, scope, ownership, no false production claims | DONE |
| I01 | Trading domain map | actors, order lifecycle, market-access capabilities, glossary | NEXT |
| I02 | Protocol/session architecture | FIX/FIXT concepts, session state, sequence/recovery, native adapter boundary | PLANNED |
| I03 | OMS / EMS / SOR / pre-trade risk | component responsibilities, deterministic control path, fail-closed strategy | PLANNED |
| I04 | Market data | feed handlers, normalization, book state, reference data, replay | PLANNED |
| I05 | Latency engineering | latency budget, p50/p95/p99/p99.9, jitter, timestamping, saturation model | PLANNED |
| I06 | Hybrid placement | colo/on-prem/cloud decision matrix, data gravity, egress, security | PLANNED |
| I07 | Resilience | gateway redundancy, session failover, replay, kill switch, degraded modes | PLANNED |
| I08 | Observability | latency telemetry, SLI/SLO, tracing boundaries, packet/app metrics | PLANNED |
| I09 | Security | entitlements, secrets/keys, network zones, audit, segregation of duties | PLANNED |
| I10 | Synthetic runtime | paper order flow + gateway simulator + latency instrumentation | PLANNED |
| I11 | Evidence | load/failure tests, latency histograms, recovery measurements, runbooks | PLANNED |
| I12 | Interview/demo pack | 15-min demo, diagrams, trade-offs, limitations, portfolio graduation | PLANNED |

## Reuse / Adapt / New

### REUSE
- TradeOps deterministic Risk Gate concepts and paper-only workflow.
- Redpanda/Kafka integration patterns for non-hot-path eventing.
- OpenTelemetry/Prometheus/Grafana observability patterns.
- Azure hybrid architecture patterns from the MayaBank Azure repository.

### ADAPT
- Existing OMS/paper execution semantics into a protocol-neutral Market Access simulator.
- Existing architecture governance and evidence conventions.
- Existing GitOps/CI patterns for non-latency-critical services.

### NEW
- FIX/FIXT session model.
- exchange-adapter boundary;
- order gateway state machine;
- low-latency budget model;
- colocation placement model;
- deterministic pre-trade controls in the hot path;
- latency/jitter evidence pack;
- Market Access failure modes and recovery scenarios.

## Graduation rule

The repository may be described as **PORTFOLIO_READY** only when I12 is complete.

Before then:
- architecture diagrams may be presented as reference design;
- implemented code may be presented as synthetic lab;
- no HFT, venue certification, production exchange connectivity or production low-latency claim is allowed without evidence.
