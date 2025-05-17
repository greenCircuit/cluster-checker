#!/bin/bash
git remote -v
project=${1}
git remote add  gitlab  "http://gitlab.dev.local/homelab/${project}"

git remote set-url --add --push origin http://gitlab.dev.local/homelab/${project}
git remote set-url --add --push origin https://github.com/greenCircuit/${project}

