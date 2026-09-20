#!/bin/bash

if [ $# -eq 1 ]; then
    if [ $1 = "prod" ]; then
        echo "running in prod"
    else 
        echo "not prod"
    fi
else echo "too many arguments, should only be 1. You entered $#"
fi
