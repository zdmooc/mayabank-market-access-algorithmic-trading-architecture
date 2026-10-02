# I09 — Security, Entitlements and Audit

## Security goals

Market Access security must protect the ability to:
- create orders;
- cancel/replace orders;
- alter routing;
- change risk limits;
- change venue session configuration;
- activate/deactivate gateways;
- access keys/credentials;
- deploy hot-path binaries.

## Controls

### Identity and access
- named operator identities;
- least privilege;
- privileged-role separation;
- strong authentication for control-plane actions;
- separate machine identities for gateways.

### Secrets and keys
- centralized lifecycle;
- rotation;
- no secrets in Git;
- runtime injection;
- controlled emergency access.

### Network segmentation
- venue-facing zone;
- trading application zone;
- management/control plane;
- observability plane;
- enterprise/cloud connectivity.

### Change control
Hot-path changes require:
- traceable version;
- peer review;
- reproducible build;
- controlled promotion;
- rollback;
- evidence that config and binary versions match the approved release.

### Audit
Capture:
- order intent;
- risk decision;
- route;
- gateway/session;
- execution response;
- operator action;
- config change;
- deployment;
- kill-switch action.

## Safety boundary

AI/LLM components must never be inserted into the deterministic order hot path solely because the wider portfolio contains GenAI capabilities.

AI may support:
- incident analysis;
- runbook assistance;
- anomaly triage;
- post-trade analytics;
- documentation.

Deterministic controls remain authoritative.
