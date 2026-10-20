# Services

All services are small FastAPI apps with:
- `/healthz` endpoint
- Kafka producer/consumer loops (kafka-python)
- Optional Postgres persistence

Images are built and pushed by:
- `make build`
- `make push`

In OpenShift, manifests expect images in the internal registry:
`image-registry.openshift-image-registry.svc:5000/trading-apps/<service>:0.1.0`
