# I01 — Order Lifecycle and Market Access Flow

## End-to-end order lifecycle

```text
1. Signal / trader intent
2. OMS order creation
3. EMS/SOR execution decision
4. deterministic pre-trade risk
5. venue selection
6. market-access gateway
7. FIX/FIXT or venue-native session
8. venue acknowledgement
9. partial/full execution
10. execution report / drop copy
11. OMS state update
12. audit / surveillance / downstream events
```

## Critical states

A simplified order state machine:

```text
NEW
 -> RISK_ACCEPTED
 -> SENT
 -> ACKNOWLEDGED
 -> PARTIALLY_FILLED
 -> FILLED

Alternative paths:
NEW -> RISK_REJECTED
SENT -> REJECTED
ACKNOWLEDGED -> CANCEL_PENDING -> CANCELLED
ACKNOWLEDGED -> REPLACE_PENDING -> REPLACED
UNKNOWN -> RECONCILIATION_REQUIRED
```

## Session architecture

For session-oriented market connectivity, architecture must manage:
- logon/logoff;
- heartbeats;
- sequence numbers;
- resend requests;
- duplicate detection;
- gap recovery;
- persistence of session state;
- recovery after process/host failover;
- venue-specific throttling and session limits.

FIX/FIXT is treated as one protocol family. Real venues may also require proprietary/native binary protocols. Adapters therefore sit behind a stable internal order/execution contract.

## Internal canonical contract

The internal canonical model should preserve:
- client order ID;
- venue order ID;
- instrument;
- side;
- quantity;
- order type;
- limit/stop attributes;
- time-in-force;
- timestamps at each boundary;
- risk decision;
- route/venue;
- execution state;
- rejection reason;
- correlation IDs.

## Fail-safe principle

If risk state is unavailable or session state is ambiguous, the architecture must prefer explicit degraded modes over silent execution.

Typical actions:
- reject new orders;
- allow cancels only;
- suspend one venue;
- switch to alternate gateway;
- require reconciliation before resuming.


## I01 deep-dive package

The complete I01 learning and architecture pack is under [docs/i01/](i01/README.md).

FIX session internals (sequence gaps, Resend Request, Gap Fill, persistent session recovery, FIXT/FIXP) are deliberately deferred to I02 and must not be marked complete before I01 human validation.
