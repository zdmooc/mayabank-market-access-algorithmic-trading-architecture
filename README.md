# MayaBank Market Access & Algorithmic Trading Architecture

Reference architecture and interview-ready lab for **electronic trading / market access transformation**.

This repository focuses on the architecture boundary between:

- trading applications and algorithmic execution;
- OMS / EMS / SOR;
- pre-trade risk controls;
- market-access gateways;
- FIX / FIXT and exchange-native protocol adapters;
- market-data ingestion;
- low-latency infrastructure and colocation;
- on-premise / colocation / cloud placement;
- resilience, observability, security and operational evidence.

## Mission-driven origin

This repository was created from a real market signal for a **Senior Architect — Market Access / Algorithmic Trading** transformation mission involving performance, rationalisation and a target architecture spanning **cloud, on-premise and colocation**.

The repository is intentionally provider-neutral and does **not** claim to reproduce any client's internal architecture.

## Truth model

This project is a **REFERENCE ARCHITECTURE / PORTFOLIO LAB**.

It does not claim:

- production HFT experience;
- direct connectivity to a real exchange;
- exchange certification;
- production multicast market-data feeds;
- kernel-bypass / FPGA / RDMA runtime proof;
- real-money autonomous trading.

Any executable component added here must remain simulated, paper-only or synthetic unless explicit evidence states otherwise.

## Scope

```text
Trader / Strategy / Algo
        |
        v
   OMS / EMS / SOR
        |
        v
 Pre-Trade Risk Gate
        |
        v
 Market Access Gateway
   |            |
   | FIX/FIXT   | Native Protocol
   v            v
 Broker / Venue / Exchange

Parallel planes:
- Market Data
- Reference Data
- Drop Copy / Execution Reports
- Surveillance / Audit
- Observability / Latency Telemetry
- CI/CD / Security / Configuration
```

## Core architectural principle

The target architecture separates workloads by latency sensitivity.

```text
COLOCATION / HOT PATH
- venue gateways
- protocol adapters
- deterministic pre-trade checks
- low-latency market data handlers
- latency-critical routing/execution

ON-PREMISE / NEAR PATH
- OMS/EMS services
- reference data
- risk aggregation
- operational control
- integration with enterprise systems

CLOUD / ELASTIC PLANE
- analytics
- historical data
- observability
- reporting
- CI/CD
- non-latency-critical risk workloads
- model training / experimentation
```

Cloud is therefore treated as a placement option, not as a blanket migration target.

## Repository boundaries

### This repository owns

- market-access reference architecture;
- latency budget and performance engineering;
- colocation / on-prem / cloud placement;
- protocol/session architecture;
- deterministic pre-trade risk placement;
- market-data and execution-report flow;
- resilience and degraded-mode design;
- latency observability and SLOs;
- interview/demo material for Market Access architecture.

### Portfolio ownership and consumption model

**PRODUCT_OWNED**

- Market Access hot path;
- FIX/session/sequence/recovery semantics;
- deterministic pre-trade risk;
- execution-oriented Market Data path;
- Drop Copy/reconciliation;
- latency/time evidence and hybrid placement decisions.

**CONSUME_SHARED — outside the latency-critical hot path**

- identity/OIDC contract;
- OpenTelemetry/observability contract;
- secrets/PKI conventions;
- GitOps conventions;
- quality gates.

The canonical declaration is `platform-consumption/capability-consumption.yaml`, using the portfolio `CapabilityConsumption` API `platform.mayabank.example/v1alpha1`.

**REFERENCE_ONLY**

- `TradeOps-GenAI-Integration` — paper/shadow workflow and AI/HITL reference;
- `mayabank-kafka-ddd-openshift` — eventing/audit/replay reference outside the synchronous order path;
- `mayabank-azure-cloud-ai-platform` — Azure/hybrid patterns;
- `mayabank-api-management-architecture` — control/admin/reporting API patterns only.

**LEGACY**

- `openshift2026-openshift-local-trading-gateway` remains archived/historical and is not revived as the primary proof for this mission.

### Shared Platform boundary

`CapabilityConsumption` is the canonical Kubernetes Platform API in the current portfolio governance. This repository declares intent only; it does not claim a Market Access Kubernetes/OpenShift deployment or Platform Operator runtime evidence.

Shared capabilities must not become synchronous dependencies of:

```text
Order → Pre-Trade Risk → Market Access Gateway → Venue
```

OIDC, OTel, GitOps, secrets and quality integration belong to control/near/elastic planes unless explicit latency evidence justifies otherwise.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

Current target:

- **I00** scope, truth model and repository boundaries;
- **I01** Market Access domain + order lifecycle + OMS/EMS/SOR/Gateway boundaries + Drop Copy + pre-trade controls;
- **I02** FIX/FIXT session model, sequence/recovery, FIXP principles and native-adapter boundary;
- **I03** Market Data, feed handlers, entitlements and distribution;
- **I04** pre-trade controls + MiFID II / RTS 6 traceability;
- **I05** time architecture + latency/jitter/NFR;
- **I06** RUN, incidents and exchange/venue migrations;
- **I07** colocation / on-prem / cloud placement;
- **I08** resilience, HA/DR and degraded modes;
- **I09** security, entitlement, audit and observability;
- **I10** executable synthetic lab — IMPLEMENTED / paper-only;
- **I11** performance and failure evidence pack;
- **I12** interview/demo pack and portfolio graduation.

## Current status

**I00→I12 COMPLETE / PORTFOLIO_READY / SYNTHETIC CI EVIDENCE PASS**

I01 was explicitly validated by the repository owner on 2026-10-02 after review with the architecture schema. Interview questions remain a rehearsal activity. I02→I12 are now implemented as architecture, synthetic runtime, evidence and interview assets.

No production Market Access runtime is claimed.

## Documentation

- [Scope & truth model](docs/00-scope-and-truth-model.md)
- [Reference architecture](docs/01-reference-architecture.md)
- [Order and Market Access flow](docs/02-market-access-flow.md)
- [I01 complete learning pack](docs/i01/README.md)
- [Regulatory / time / protocol baseline](docs/08-regulatory-time-protocol-baseline.md)
- [Latency engineering](docs/03-latency-engineering.md)
- [Hybrid placement](docs/04-hybrid-placement.md)
- [Resilience & observability](docs/05-resilience-observability.md)
- [Security controls](docs/06-security-controls.md)
- [Interview pack](docs/07-interview-pack.md)
- [I02 — FIX / session / recovery](docs/i02/README.md)
- [I03 — Market Data / entitlements](docs/i03/README.md)
- [I04 — Pre-trade controls / regulation](docs/i04/README.md)
- [I05 — Time / latency / NFR](docs/i05/README.md)
- [I06 — RUN / incidents / venue migration](docs/i06/README.md)
- [I07 — Hybrid placement](docs/i07/README.md)
- [I08 — Resilience / HA-DR](docs/i08/README.md)
- [I09 — Security / observability](docs/i09/README.md)
- [I10 — Synthetic runtime](docs/i10/README.md)
- [I11 — Evidence](docs/i11/README.md)
- [I12 — Interview / demo](docs/i12/README.md)
- [I12 — Interview answer key](docs/i12/interview-answer-key.md)
- [CI evidence 2026-10-02](evidence/CI_EVIDENCE_2026-10-02.md)
- [ADR-001 — Keep the latency-critical hot path close to venues](adr/ADR-001-hot-path-placement.md)
- [ADR-002 — Do not treat cloud migration as a blanket target](adr/ADR-002-cloud-boundary.md)

## Disclaimer

MayaBank is a fictional portfolio environment. Product names and public protocols may be referenced for learning and architecture comparison. No confidential client architecture is represented here.


## Completion baseline — 2026-10-02

The I02→I12 baseline is implemented:
- I02 FIX/FIXT/FIXP session, sequence and recovery architecture;
- I03 Market Data, book/recovery and entitlements;
- I04 deterministic pre-trade controls and regulatory traceability;
- I05 time architecture, latency and jitter;
- I06 RUN, incidents, RCA and venue migration;
- I07 colocation/on-prem/cloud placement;
- I08 resilience, HA/DR and degraded modes;
- I09 security, audit and observability;
- I10 executable synthetic Python lab;
- I11 automated failure/performance evidence harness;
- I12 interview/demo pack.

Truth boundary: the runtime is synthetic/paper-only. It does not prove production HFT, direct exchange connectivity, venue certification, production multicast Market Data or production low-latency performance.


## Synthetic evidence — PASS

GitHub Actions run `37043637911` — **SUCCESS** on commit `9d589b7457032fc22c8f9e537f851626979a000d`.

Observed:
- 10 automated tests — PASS;
- demo: ORD-1 FILLED 10000/0, ORD-2 REJECTED MAX_QTY;
- synthetic risk-check benchmark: 5,000 samples;
- p50 1.012 µs; p95 1.854 µs; p99 2.656 µs; p99.9 9.336 µs; max 27.892 µs; mean 1.122 µs.

These timings are **PERFORMANCE_MEASURED_SYNTHETIC_ONLY** on a GitHub-hosted runner. They are not venue, network, FIX-engine or production-HFT latency measurements.


## H1 — Platform alignment — 2026-10-04

Status: **STATIC_CONSUMER_CONTRACT_VERIFIED**.

The repository now exposes a `platform-consumption/` profile aligned with D-091/D-093:

- `CapabilityConsumption` v1alpha1 declaration;
- `PRODUCT_OWNED` Market Access domain capabilities;
- shared identity/observability/secrets/GitOps/quality intent;
- Kafka/Azure/API Management/TradeOps kept `REFERENCE_ONLY`;
- `Observe` + `Retain` lifecycle;
- no embedded shared-service endpoint or secret;
- no claim of CRC/OpenShift deployment.

Contract promotion: **STATIC_CONSUMER_CONTRACT_VERIFIED** — GitHub Actions run `37224536855` SUCCESS, including 6 platform-consumption contract tests.


## H1 evidence — PASS

GitHub Actions run `37224536855` on commit `b165f22ea72b4aa4ece94d4a5d88d3d3ceeb6519` completed **SUCCESS**.

Observed:
- 16 total automated tests — PASS;
- 6 new platform-consumption contract tests included;
- synthetic demo and benchmark still pass;
- no CRC/OpenShift runtime claim is promoted.

H1 final status: **STATIC_CONSUMER_CONTRACT_VERIFIED**.
