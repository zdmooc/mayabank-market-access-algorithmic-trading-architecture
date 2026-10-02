# I04 — Deterministic Pre-Trade Controls & Regulatory Traceability

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

Controls cover instrument/permission, quantity, notional, price collar, position/credit, market/route state, message throttling and selective kill.

```text
requirement → policy/control → component → config/version
            → input values → decision → timestamp → test → evidence
```

Selective kill requires a reliable active-order index by algorithm, trader, desk, client/account, venue, instrument or route.

Regulatory mapping baseline: MiFID II Article 17, Delegated Regulation (EU) 2017/589 (RTS 6), MiFIR Article 22c and Delegated Regulation (EU) 2025/1155 for current clock-synchronization requirements. This is architecture mapping, not legal certification.

Critical-control failure modes prefer reject-new, cancel-only, route-disable, selective kill or operator approval over silent fail-open.
