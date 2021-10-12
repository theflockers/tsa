#!/usr/bin/env bash

export DOCKER_CONFIG="$(pwd)"

python3 $(which ansible-playbook) -i localhost, ansible/run.yaml -e \
    'ansible_python_interpreter=/home/leandro/Devel/redhat/venv/bin/python3' $@
