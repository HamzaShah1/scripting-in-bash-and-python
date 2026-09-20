#!/bin/bash

for domain in $@; do
echo "checking $domain"
    if ping -c 1 $domain > /dev/null; then
        echo "$domain is reachable"
    else
        echo "$domain is NOT reachable"
    fi
done