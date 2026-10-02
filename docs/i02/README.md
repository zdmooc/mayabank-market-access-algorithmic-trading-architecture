# I02 — FIX / FIXT / FIXP, sessions, sequences and recovery

Status: **IMPLEMENTED — REFERENCE_ARCHITECTURE**

## Core model

A TCP/TLS connection is transport. A trading session is a logical protocol relationship with state that may survive a disconnect.

Persist:
- sender/target identity;
- next outgoing and expected incoming sequence;
- messages required for replay;
- order/session correlation;
- recovery/logon metadata.

```text
connect → Logon → traffic
                 ├─ Heartbeat / Test Request
                 ├─ sequence-gap detection
                 ├─ Resend Request / replay
                 └─ Gap Fill where policy allows
        → Logout/disconnect → reconnect with state
```

If expected inbound sequence is 42:
- receive 42 → accept;
- receive 45 → gap 42–44 semantics require recovery of missing range before authoritative continuation;
- receive below expected → duplicate/replay handling.

A reconnect is not automatically a new session. Incorrect sequence reset is a controlled-risk operation, not a convenient fix.

## Protocol landscape

- FIX Session: stateful ordered session semantics.
- FIXT: separates session semantics from application-version selection.
- FIXP: high-performance session-family concept; production experience is not claimed.
- native binary: isolated behind venue adapters.

## Exit criteria

Explain session vs connection, gap/replay/duplicate handling, persistent restart, reset risk, and FIX/FIXT/FIXP/native boundaries.
