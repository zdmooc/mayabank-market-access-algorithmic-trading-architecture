# I08 — Resilience, HA/DR & Degraded Modes

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

Failure domains: process, host, network, gateway, session, venue, colo site, on-prem site and cloud dependency.

Gateway HA must define live-session ownership, sequence persistence, duplicate prevention, active-order reconstruction, split-brain prevention and failover authority.

Explicit modes: NORMAL, NO_NEW_ORDERS, CANCEL_ONLY, ROUTE_DISABLED, MARKET_DATA_INVALID, RECONCILIATION_REQUIRED, MANUAL_APPROVAL.

```text
detect → freeze unsafe actions → recover session/order state
       → compare Drop Copy → reconcile → validate risk/time/data → resume
```

RTO/RPO are business-service requirements; a secondary site is not evidence until failover/reconciliation is tested.
