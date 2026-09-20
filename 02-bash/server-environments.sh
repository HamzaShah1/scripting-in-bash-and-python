#!/bin/bash

echo "$(cut -d "," -f 2 $1 | sort | uniq -c)"