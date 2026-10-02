# I07/I08 — Resilience and Observability

## Failure domains

Design explicitly for:
- gateway process crash;
- host loss;
- NIC/link failure;
- venue session disconnect;
- sequence gap;
- partial network partition;
- stale market data;
- clock drift;
- risk service unavailable;
- OMS unavailable;
- duplicate execution report;
- delayed drop copy;
- primary datacenter failure.

## Recovery patterns

- active/standby gateway with explicit session ownership;
- deterministic session-state recovery;
- durable sequence/checkpoint state;
- replay and reconciliation;
- cancel-on-disconnect when supported and appropriate;
- venue isolation;
- kill switch;
- "cancel-only" degraded mode;
- independent health of order and market-data channels.

## Observability model

### Hot-path telemetry
Keep overhead bounded:
- monotonic timestamps;
- protocol/session counters;
- send/ack round-trip latency;
- serialization time;
- risk evaluation latency;
- queue depth;
- retransmit/gap counters;
- disconnect/reconnect counters.

### Enterprise telemetry
- Prometheus/OpenTelemetry-compatible aggregation;
- Grafana dashboards;
- centralized logs;
- audit events;
- deployment/version metadata;
- capacity and saturation indicators.

## Example SLI

```text
order_gateway_ack_latency_ms
risk_evaluation_latency_us
venue_session_disconnect_total
fix_resend_request_total
market_data_gap_total
orders_rejected_risk_total
orders_unknown_state_total
clock_offset_us
```

## SLO rule

Targets must be derived from business/venue requirements and measured baselines. This repository intentionally avoids inventing universal microsecond thresholds.

## DR distinction

High availability near one venue does not equal disaster recovery.

Document separately:
- process HA;
- host HA;
- rack/site HA;
- datacenter recovery;
- alternative venue/routing;
- state reconciliation after disaster.
