# ADR-002 — Treat cloud as an elastic plane, not a mandatory execution venue

## Status
Accepted as reference-architecture principle.

## Context
Cloud provides elasticity, managed services, analytics capabilities and operational automation, but network distance and shared infrastructure can conflict with strict deterministic-latency requirements.

## Decision
Use cloud first for workloads that benefit from elasticity and are not constrained by venue-proximity latency:
- historical data;
- analytics/backtesting;
- observability backends;
- reporting;
- CI/CD;
- model training;
- selected risk/enterprise services.

Evaluate execution-path workloads separately.

## Consequences
- hybrid architecture is expected;
- network and data-transfer costs become explicit;
- resilience spans multiple operational domains;
- no component is placed in cloud solely for strategic branding.
