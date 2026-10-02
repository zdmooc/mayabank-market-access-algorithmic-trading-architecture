# ADR-001 — Keep the latency-critical hot path close to the venue

## Status
Accepted as reference-architecture principle.

## Context
Market Access transformation may span cloud, enterprise datacenters and colocation. Some workloads are highly sensitive to latency and jitter.

## Decision
Do not move the execution hot path away from the venue without measured evidence that the target placement satisfies the latency and resilience requirements.

The hot path includes, depending on architecture:
- venue gateway;
- protocol adapter;
- deterministic pre-trade controls;
- latency-critical routing/execution;
- critical market-data handling.

## Consequences
- cloud adoption remains possible around the hot path;
- migration is workload-specific;
- latency must be baselined before placement decisions;
- operational complexity of colocation is accepted where justified.

## Rejected alternative
Blanket "cloud-first means cloud-everything" migration.
