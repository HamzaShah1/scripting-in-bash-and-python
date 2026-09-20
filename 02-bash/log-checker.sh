#!/bin/bash

checker(){
    echo "Log file: $1"

    if [ -e "$1" ]; then
        echo "Errors found: $(grep -c "ERROR" "$1")"
        return 0
    else
        echo "the Log file: $1, does not exist"
        return 1
    fi
}

checker $1