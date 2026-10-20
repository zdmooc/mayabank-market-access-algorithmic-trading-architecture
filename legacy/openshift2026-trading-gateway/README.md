# OpenShift Local Trading Gateway (CRC)

A lab-grade platform repository that applies a **“Gateway / Platform Ownership”** architecture to **trading** on **OpenShift Local (CRC)**.

- Event-driven backbone (Kafka-compatible bus) via **Redpanda** (light mode for CRC)
- Stateful services via **PostgreSQL**
- Optional **Keycloak** (OIDC) for SSO/IAM
- Microservices (Python) for market data simulation, bar aggregation, strategy, risk, OMS, paper broker
- Kustomize overlays and bootstrap scripts

> This repository is a **POC/lab**. It is not HFT/low-latency and does not implement real-money trading compliance.

## Quickstart
```bash
oc login -u kubeadmin -p <PASSWORD> https://api.crc.testing:6443

make bootstrap
make registry-login
make build
make push
make deploy
make demo
```

## Documentation
- `docs/architecture.md`
- `docs/runbooks.md`
- `docs/api_examples.md`

## Repo map
- `cluster/` : namespaces, quotas, platform manifests
- `deploy/` : kustomize base + overlay
- `services/`: microservices (FastAPI) + Dockerfiles
- `scripts/` : bootstrap/build/deploy/demo helpers
