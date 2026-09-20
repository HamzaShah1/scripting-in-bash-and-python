#!/bin/bash

if [ "$#" -eq 1 ]; then
    if [ -f "$1" ]; then
        echo "file exists"
    else
        echo "file doesnt exist"
    fi
else
    echo "too many filenames entered"
fi