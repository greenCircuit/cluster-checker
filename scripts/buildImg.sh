#!/bin/bash

TAG="latest"
export CI_REGISTRY_IMAGE="registry.dev.local/homelab/cluster-checker"
full_path="${CI_REGISTRY_IMAGE}:${TAG}"
podman login "$CI_REGISTRY_IMAGE" -u "${GITLAB_USER}" -p "${GITLAB_TOKEN}"
podman build -t "${full_path}" .
podman push "${full_path}"