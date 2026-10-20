SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

help:
	@echo "Targets:"
	@echo "  make bootstrap         - Create namespaces + deploy platform (redpanda + postgres)"
	@echo "  make registry-login    - Login to OpenShift internal registry for podman"
	@echo "  make build             - Build local images with podman"
	@echo "  make push              - Push images to OpenShift internal registry"
	@echo "  make deploy            - Deploy apps (kustomize overlay dev)"
	@echo "  make demo              - Run a short demo (create order + watch states)"
	@echo "  make clean             - Delete namespaces (WARNING)"

bootstrap:
	./scripts/10_bootstrap_cluster.sh

registry-login:
	./scripts/15_registry_login.sh

build:
	./scripts/20_build_images.sh

push:
	./scripts/25_push_images.sh

deploy:
	./scripts/30_deploy_apps.sh

demo:
	./scripts/40_demo.sh

clean:
	./scripts/90_clean.sh
