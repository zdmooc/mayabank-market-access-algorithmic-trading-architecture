# I03 — Market Data & Entitlements

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

```text
Venue/Vendor → Feed Handler → Sequence/Gap Detection → Normalize
             → Book Builder → Quality/Staleness → Trader/Algo/SOR
```

Architecture distinguishes snapshot, incremental updates, gap detection, recovery and stale-data state. An unresolved gap invalidates the local book until deterministic recovery.

Entitlements are modeled by consumer identity, provider, venue, service, content type, real-time/delayed status, depth/snapshot/full-tick rights and redistribution rights.

Current documentation uses RTDS/RTMDS terminology; TREP/RMDS stay legacy/search vocabulary.

Fail-safe examples: stale data blocks/downgrades routing, unresolved gap marks the book invalid, unauthorized content is denied and audited.
