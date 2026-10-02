# I09 — Security, Audit & Observability

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

Security boundaries: operator/service identity, least privilege, certificates/keys, secrets lifecycle, network segmentation, route/venue authorization, change control and segregation of duties.

Hot-path telemetry uses bounded counters/timestamps at order receive, risk decision, gateway enqueue/dequeue, encode/send, venue response, decode and OMS update.

SLIs include order/gateway/ack latency, risk latency, disconnects, sequence gaps, resend, rejects, throttling, stale-data duration, clock offset and reconciliation mismatches.

No universal microsecond SLO is invented. OpenTelemetry/Prometheus/Grafana are backend/shared capabilities, not synchronous hot-path dependencies.
