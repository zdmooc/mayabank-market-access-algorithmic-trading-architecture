# I05 — Latency Engineering

## Why averages are insufficient

Electronic-trading systems are sensitive not only to mean latency but to tail latency and jitter.

Track at minimum:
- p50;
- p95;
- p99;
- p99.9 where sample volume permits;
- max;
- jitter;
- timeout/error rate;
- queue depth and saturation.

## Latency budget model

```text
T_total =
  T_strategy_to_oms
+ T_oms_to_sor
+ T_risk
+ T_gateway
+ T_protocol_encode
+ T_network_to_venue
+ T_venue_response
+ T_network_return
+ T_protocol_decode
+ T_state_update
```

Each segment needs:
- measurement point;
- timestamp source;
- owner;
- target;
- warning threshold;
- hard limit;
- evidence method.

## Infrastructure concerns

Architecture topics to evaluate when justified by target latency:
- NUMA topology;
- CPU isolation/pinning;
- scheduler interference;
- IRQ affinity;
- NIC queues;
- RSS/RPS/XPS;
- huge pages;
- memory allocation behavior;
- GC strategy for managed runtimes;
- network interrupt moderation;
- PTP hardware timestamping;
- kernel/network tuning;
- kernel-bypass technologies where evidence justifies complexity.

These are architecture options, not default requirements.

## Measurement principles

- synchronize clocks;
- distinguish application timestamps from packet timestamps;
- test steady state and bursts;
- capture warm-up effects;
- measure under failure/recovery;
- retain raw evidence;
- never compare synthetic local measurements directly with production venue SLAs.

## Performance decision gate

A technology optimization is accepted only if:
1. a latency bottleneck is measured;
2. the optimization targets that bottleneck;
3. operational complexity is documented;
4. rollback exists;
5. the gain is reproducible.
