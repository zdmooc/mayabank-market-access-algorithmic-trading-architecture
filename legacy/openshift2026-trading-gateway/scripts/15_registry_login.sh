#!/usr/bin/env bash
set -euo pipefail

oc patch configs.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"defaultRoute":true}}' >/dev/null || true
REGISTRY_HOST="$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}' 2>/dev/null || true)"

if [[ -z "${REGISTRY_HOST}" ]]; then
  echo "Registry route not ready yet. Try again."
  exit 1
fi

TOKEN="$(oc whoami -t)"
USER="$(oc whoami)"

echo "Logging into registry: ${REGISTRY_HOST}"
podman login --tls-verify=false -u "${USER}" -p "${TOKEN}" "${REGISTRY_HOST}"
echo "Registry login OK"
