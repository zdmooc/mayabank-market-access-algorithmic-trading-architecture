# I01 — Market Access Domain & Order Lifecycle

Status: **CONTENT_COMPLETE / HUMAN_VALIDATION_PENDING**

I01 converts the Market Access mission signal into a business/domain architecture pack. It deliberately avoids FIX session internals beyond the minimum vocabulary; those belong to I02 after human validation.

## Deliverables

1. [Domain and actors](01-domain-and-actors.md)
2. [OMS / EMS / SOR / Gateway boundaries](02-oms-ems-sor-gateway-boundaries.md)
3. [Happy-path order lifecycle](03-order-lifecycle-happy-path.md)
4. [Reject / Cancel / Cancel-Replace](04-reject-cancel-replace-sequences.md)
5. [Simplified order state machine](05-order-state-machine.md)
6. [Drop Copy and reconciliation](06-drop-copy-reconciliation.md)
7. [Pre-trade control matrix](07-pre-trade-control-matrix.md)
8. [60-term glossary](08-glossary.md)
9. [Ten incident scenarios](09-incident-scenarios.md)
10. [Human validation checklist](10-validation-checklist.md)

## Exit gate

I01 is not DONE merely because the files exist.

It becomes **VALIDATED** only when the architect can explain the 20 mandatory questions and whiteboard exercise in [10-validation-checklist.md](10-validation-checklist.md) without notes.

Until then:
- I01 = CONTENT_COMPLETE / HUMAN_VALIDATION_PENDING
- I02 = BLOCKED BY I01 HUMAN VALIDATION
- I10 simulator = DEFERRED
