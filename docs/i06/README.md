# I06 — RUN, Incidents, RCA & Venue Migration

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

RUN separates venue/session, order flow, Market Data, risk, time sync, infrastructure and downstream/audit health.

Incident priority: protect client/market → stop unsafe new flow → preserve/cancel active orders → restore authoritative state → reconcile → controlled resume → RCA/evidence.

Runbooks cover disconnect, sequence gap, ambiguous order, stale Market Data, Drop Copy divergence, risk unavailable, throttle saturation, clock drift, venue outage and gateway failure.

Venue migration gates: spec review → adapter → conformance-style synthetic tests → replay → performance baseline → runbook → controlled cutover/rollback. No venue certification is claimed.
