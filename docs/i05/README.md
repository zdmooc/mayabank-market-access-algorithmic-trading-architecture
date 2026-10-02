# I05 — Time Architecture, Latency, Jitter & NFR

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

```text
UTC reference → time source → NTP/PTP → host/NIC clocks
              → application timestamps → end-to-end event correlation
```

Track source traceability, offset, drift, holdover, alarms, hardware/software timestamp point and precision.

Latency budget:
```text
T_total = T_OMS + T_risk + T_router + T_gateway + T_encode
        + T_network + T_venue + T_return + T_decode
```

Report p50/p95/p99/p99.9 where sample size supports it, max, jitter/dispersion, throughput and saturation. Do not optimize averages alone.

CPU affinity/NUMA/IRQ/NIC queues/GC/kernel tuning/hardware timestamps/kernel-bypass are architecture topics, not production claims.
