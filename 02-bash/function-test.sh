#!/bin/bash

greet(){
    if [ "$#" -eq 1 ]; then
        echo "hello $1"
        return 0
    elif [ "$#" -gt 1 ]; then
        echo "too many names"
        return 1
    else
        echo "name not provided"
        return 1
    fi
}

greet hamza
greet alice
greet bob hamza jim
greet

exit 0