# I12 — Interview Pack

## 60-second positioning

"I would not start by moving Market Access to cloud. I would first separate the latency-critical hot path from the enterprise and analytical planes, baseline latency and failure modes, then decide placement workload by workload. Venue gateways, protocol adapters and deterministic pre-trade controls may need to remain close to the venue, while observability, historical data, analytics, CI/CD and other non-critical workloads can benefit from cloud elasticity."

## Questions to ask the client

1. Which asset classes and venues are in scope?
2. Where are the gateways physically hosted today?
3. Which protocols are used: FIX/FIXT, native binary, proprietary APIs?
4. What are the current p50/p99/p99.9 order/ack latencies?
5. What is the accepted jitter budget?
6. Is market data direct, vendor-mediated or both?
7. What are the current OMS, EMS and SOR responsibilities?
8. Where are pre-trade controls executed?
9. How are session sequence/recovery and drop copy handled?
10. What is the failover model for a gateway or colocation site?
11. Which workloads are already cloud-hosted?
12. What exactly is expected from the architect: AS-IS, target, rationalisation, roadmap, performance benchmark, migration governance?
13. Is the objective cost reduction, performance improvement, simplification, resilience, cloud adoption, or all of them?
14. What are the hard constraints that must not change?
15. What evidence is required before a workload can move?

## Architecture discussion points

Be ready to explain:
- why market-access hot paths differ from ordinary microservices;
- why tail latency matters;
- how sequence/state recovery affects HA;
- why Kafka is valuable around the hot path but not automatically inside it;
- how to design hybrid placement;
- how to modernize without pretending that every component belongs on Kubernetes;
- how to measure improvement.

## Truthful portfolio statement

Use:
- historical products-derivatives experience as domain context;
- recent architecture/transformation experience as the core senior-architect proof;
- this repository as a current reference architecture/lab.

Do not claim recent production HFT or direct exchange connectivity unless documented separately.


## I01 validation before specialist claims

Before presenting the repository as a validated Market Access learning asset, pass the I01 human gate in `docs/i01/10-validation-checklist.md`.

The repository may currently be described as:
- mission-aligned reference architecture;
- I01 content complete;
- human validation pending.

Do not describe I01 as mastered or validated until that gate is passed.
