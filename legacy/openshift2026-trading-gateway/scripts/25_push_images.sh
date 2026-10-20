#!/usr/bin/env bash
set -euo pipefail

REGISTRY_HOST="$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')"
NAMESPACE="trading-apps"

SERVICES=(
  market-data-adapter
  bar-aggregator
  strategy-runner
  risk-engine
  order-manager
  broker-adapter-paper
)

echo "Pushing images to ${REGISTRY_HOST}/${NAMESPACE} ..."
for s in "${SERVICES[@]}"; do
  podman tag "${s}:0.1.0" "${REGISTRY_HOST}/${NAMESPACE}/${s}:0.1.0"
  podman push --tls-verify=false "${REGISTRY_HOST}/${NAMESPACE}/${s}:0.1.0"
done

echo "Push OK"
