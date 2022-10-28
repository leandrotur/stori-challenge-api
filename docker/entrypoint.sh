#!/usr/bin/env bash
set -e

PROG=$(basename $0)
echo "Executing: $0 $1 $2"

if [[ $1 == "app" ]]; then
    if [[ $2 == "test" ]]; then
        flake8
        coverage run -m pytest --tb=auto -vv
        coverage report
        coverage xml
    elif [[ $2 == "start" ]]; then
        python /app/main.py
    fi
fi
