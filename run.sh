#!/usr/bin/env bash

PYTHON3=$(which python3)
PIP3=$(which pip3)
DOCKER_CONFIG="$(pwd)"

export PIP3 PYTHON3 DOCKER_CONFIG

${PYTHON3} $(which ansible-playbook || which ansible-playbook-3) -i localhost, ansible/run.yaml -e \
    "ansible_python_interpreter=${PYTHON3}" $@
