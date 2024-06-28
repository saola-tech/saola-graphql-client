#!/bin/bash

function create_venv {
  if [ ! -d ".venv" ]; then
    python3.9 -m venv .venv
  fi
  source .venv/bin/activate
  echo "Virtual environment activated!"
}

create_venv

python3.9 -m pip install --upgrade pip
pip3.9 install -r requirements.txt

pre-commit install -c .pre-commit-config.yaml
