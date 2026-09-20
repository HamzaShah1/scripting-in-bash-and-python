#!/bin/bash

set -euo pipefail

if [ "$#" -ne 1 ]; then 
    echo "incorrect filenames, should be = 1; supplied; $#"
    exit 1
fi

filename="$1"
echo "checking $1"
if [ -f "$1" ]; then
    if errors_found=$(grep -c "ERROR" $1) || grep_status=$?; then
        echo "errors found: $errors_found"
        echo "status: $grep_status"
    else
        echo "no errors found"
    fi
else
    echo "file doesnt exist"
    exit 1
fi

