# I00 — Scope and Truth Model

## Purpose

This repository prepares an architecture response to a Market Access / Algorithmic Trading transformation problem without overstating historical experience or runtime proof.

## Problem statement

A typical electronic-trading estate combines:
- latency-critical execution components;
- market connectivity;
- enterprise risk and control systems;
- observability and audit;
- large historical datasets;
- development and release platforms.

A transformation programme may ask which components remain in colocation, which can move to enterprise datacenters, and which are suitable for cloud.

The answer must be workload-specific.

## Evidence labels

Use only these labels:

- **REFERENCE_ARCHITECTURE** — design based on public architecture principles.
- **IMPLEMENTED** — code/manifests exist and pass static or unit checks.
- **RUNTIME_PROVEN_LOCAL** — executed in a controlled local lab.
- **PERFORMANCE_MEASURED_SYNTHETIC** — measured against synthetic traffic only.
- **PRODUCTION_TARGET** — intended production-grade design, not deployed.
- **NOT_PROVEN** — capability discussed but not demonstrated.

## Explicit exclusions

This repository does not assert:
- co-location experience with a specific venue;
- direct market membership;
- certified FIX conformance;
- native exchange protocol certification;
- FPGA/SmartNIC implementation;
- DPDK/Onload/RDMA production use;
- sub-microsecond deterministic performance;
- real-money autonomous algorithmic execution.

## Portfolio relationship

```text
TradeOps
  -> AI/GenAI + HITL + paper trading workflow

Market Access repo
  -> deterministic execution architecture
  -> protocol/session boundary
  -> latency placement
  -> colocation/on-prem/cloud transformation

Shared Platform
  -> common IAM/observability/GitOps for non-hot-path capabilities
```

## Mission fit

The target role is an architect role. The portfolio therefore emphasizes:
- AS-IS / TO-BE;
- workload placement;
- NFR and measurable latency;
- resilience and failure modes;
- migration sequencing;
- architecture decisions and trade-offs;
- operational evidence.
