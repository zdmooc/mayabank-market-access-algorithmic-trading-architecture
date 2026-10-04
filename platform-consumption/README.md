# Market Access — Shared Platform Consumption Profile

**Consumer:** `zdmooc/mayabank-market-access-algorithmic-trading-architecture`  
**Role:** Market Access / Electronic Trading specialist  
**Evidence level:** `STATIC_CONSUMER_CONTRACT_VERIFIED`

## Purpose

This profile aligns the Market Access repository with the portfolio operating model:

```text
Capability → Domain Owner → Canonical Repo → Consumer → Runtime → Evidence
```

It declares shared-platform intent without moving the latency-critical Market Access path into a generic platform.

## PRODUCT_OWNED

The Market Access repository owns:

- hot-path architecture;
- FIX/session/sequence/recovery semantics;
- deterministic pre-trade risk;
- execution-oriented Market Data path;
- Drop Copy/reconciliation;
- latency/time evidence;
- colo/on-prem/cloud placement decisions;
- synthetic Market Access lab.

## CONSUME_SHARED — outside the hot path

The target profile consumes:

- identity/OIDC contract;
- OpenTelemetry/observability contract;
- secrets/PKI conventions;
- GitOps conventions;
- quality gates.

These are control/near/elastic-plane capabilities. They are **not** synchronous dependencies of:

```text
Order → Pre-Trade Risk → Gateway → Venue
```

## REFERENCE_ONLY

- TradeOps: paper/shadow workflow and AI/HITL reference;
- Kafka/DDD: audit/replay/downstream eventing patterns;
- Azure Cloud & AI: hybrid/cloud patterns;
- API Management: control/admin/reporting API patterns.

## Lifecycle

```yaml
adoptionPolicy: Observe
deletionPolicy: Retain
```

The declaration is not applied to CRC/OpenShift in this repository. It is a consumer contract only.

## D-093 boundary

`CapabilityConsumption` is the canonical Kubernetes Platform API `platform.mayabank.example/v1alpha1`.

This repository does **not** claim:
- Platform Operator runtime for Market Access;
- managed namespace/RBAC/quota/network-policy evidence;
- Argo reconciliation for Market Access;
- Shared OIDC/OTel runtime consumption by Market Access;
- CRC/OpenShift deployment.

Those claims require separately observed runtime evidence.

## Validation

`tests/test_platform_consumption.py` verifies the required contract surface and guards against embedding shared-platform endpoints or credentials.


## Evidence

GitHub Actions run `37224536855` — **SUCCESS**.

The repository executed 16 tests, including the six `PlatformConsumptionContractTests` checks. This proves the static consumer contract shape and repository guardrails only; it does not prove a Kubernetes/OpenShift runtime consumption path.
