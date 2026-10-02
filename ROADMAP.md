# Roadmap I00 → I12

## Objective

Build a demonstrable reference architecture for a Senior Architect mission covering Market Access, Algorithmic Trading transformation, low-latency performance, rationalisation and hybrid placement across colocation, on-premise and cloud.

## Iterations

| Iteration | Scope | Exit criteria | Status |
|---|---|---|---|
| I00 | Scope, truth model, boundaries | README, scope, ownership, no false production claims | DONE |
| I01 | Market Access domain + order lifecycle | actors, OMS/EMS/SOR/Gateway boundaries, happy path, Reject/Cancel/Replace, state machine, Drop Copy, pre-trade matrix, 60-term glossary, 10 incidents, oral gate | CONTENT_COMPLETE / HUMAN_VALIDATION_PENDING |
| I02 | FIX / session / recovery | FIX/FIXT, initiator/acceptor, Logon/Logout, Heartbeat/TestRequest, MsgSeqNum, resend/gap-fill, persistence/reconnect, FIXP principles, native-adapter boundary | BLOCKED BY I01 VALIDATION |
| I03 | Market Data + entitlements | feed handlers, normalization, book state, snapshot/incremental, gap recovery, RTDS/RTMDS concepts, DACS-like entitlements | PLANNED |
| I04 | Pre-trade controls + regulation | deterministic controls, kill functionality, MiFID II Article 17, RTS 6, control-to-test evidence | PLANNED |
| I05 | Time architecture + latency/NFR | UTC traceability, NTP/PTP, timestamps, latency budget, p50/p95/p99/p99.9, jitter, saturation | PLANNED |
| I06 | RUN / incidents / migrations | operations, RCA, venue migrations, degraded modes, follow-the-sun patterns | PLANNED |
| I07 | Hybrid placement | colo/on-prem/cloud decision matrix, data gravity, egress, security | PLANNED |
| I08 | Resilience | gateway redundancy, session failover, replay, kill switch, HA/DR | PLANNED |
| I09 | Security + observability | entitlements, secrets/keys, zones, audit, latency telemetry, SLI/SLO | PLANNED |
| I10 | Synthetic runtime | paper order flow + gateway simulator + latency instrumentation | DEFERRED UNTIL I01 + I02 VALIDATED |
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


## I01 human gate

I01 is not DONE because documentation exists. It becomes VALIDATED only after the architect passes the 20-question + whiteboard checklist in `docs/i01/10-validation-checklist.md` without notes.

Current state:
```text
I00 DONE
  ↓
I01 CONTENT_COMPLETE
  ↓
HUMAN VALIDATION PENDING
  ↓
I02 BLOCKED
  ↓
I10 DEFERRED
```

## Cross-cutting baseline

The following concerns start now and are refined through later iterations:
- MiFID II Article 17 / RTS 6;
- current clock synchronisation baseline under Delegated Regulation (EU) 2025/1155, Articles 11–16 applicable from 2 March 2026;
- Market Data entitlements;
- FIX/FIXT/FIXP + encoding/framing/transport landscape.
