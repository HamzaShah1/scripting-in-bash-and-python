#!/bin/bash

if [ $# -eq 2 ]; then
    echo "two arguments were provided: $1 and $2"
else
    echo "wrong number of arguments: $#"
fi

