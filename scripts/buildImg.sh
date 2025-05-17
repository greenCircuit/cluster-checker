#!/bin/bash
podman build -t dev.io/homelab/cluster-checker:latest .
podman login -u root -p ${GITLAB_TOKEN} dev.io
podman push dev.io/homelab/cluster-checker:latest 