# Roadmap I00 → I12

## Objective

Build a demonstrable reference architecture for a Senior Architect mission covering Market Access, Algorithmic Trading transformation, low-latency performance, rationalisation and hybrid placement across colocation, on-premise and cloud.

## Iterations

| Iteration | Scope | Exit criteria | Status |
|---|---|---|---|
| I00 | Scope, truth model, boundaries | README, scope, ownership, no false production claims | DONE |
| I01 | Market Access domain + order lifecycle | actors, boundaries, lifecycle, state machine, Drop Copy, controls, glossary, incidents, oral gate | USER_VALIDATED 2026-10-02 |
| I02 | FIX / session / recovery | FIX/FIXT/FIXP, Logon/Logout, heartbeat, sequence/recovery, persistence, native boundary | IMPLEMENTED |
| I03 | Market Data + entitlements | feed handler, snapshot/incremental, book state, gap recovery, entitlements | IMPLEMENTED |
| I04 | Pre-trade controls + regulation | deterministic controls, kill functionality, regulatory traceability | IMPLEMENTED |
| I05 | Time architecture + latency/NFR | UTC, NTP/PTP, timestamping, latency budget, percentiles/jitter | IMPLEMENTED |
| I06 | RUN / incidents / venue migrations | incident playbooks, RCA, operational migration gates | IMPLEMENTED |
| I07 | Hybrid placement | colo/on-prem/cloud decision matrix and migration sequence | IMPLEMENTED |
| I08 | Resilience | session recovery, gateway redundancy, degraded/cancel-only, HA/DR | IMPLEMENTED |
| I09 | Security + observability | IAM/secrets/network/audit + SLI/SLO/telemetry | IMPLEMENTED |
| I10 | Synthetic runtime | paper order flow, risk, FIX-like session simulator, venue/drop copy | IMPLEMENTED_SYNTHETIC |
| I11 | Evidence | automated failure tests + synthetic latency benchmark + CI | IMPLEMENTED / CI_EVIDENCE_PENDING |
| I12 | Interview/demo pack | 15-minute demo, questions, trade-offs, truth matrix | IMPLEMENTED |

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
I01 USER_VALIDATED (2026-10-02)
  ↓
I02→I09 IMPLEMENTED
  ↓
I10 SYNTHETIC RUNTIME IMPLEMENTED
  ↓
I11 CI EVIDENCE PENDING
  ↓
I12 INTERVIEW PACK IMPLEMENTED
```

## Cross-cutting baseline

The following concerns start now and are refined through later iterations:
- MiFID II Article 17 / RTS 6;
- current clock synchronisation baseline under Delegated Regulation (EU) 2025/1155, Articles 11–16 applicable from 2 March 2026;
- Market Data entitlements;
- FIX/FIXT/FIXP + encoding/framing/transport landscape.


## Final completion gate

Architecture/content is implemented through I12. Portfolio graduation requires a green CI run for the synthetic runtime/evidence harness. Production-HFT and venue-connectivity claims remain excluded regardless of CI status.
