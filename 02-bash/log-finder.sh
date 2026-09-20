#!/bin/bash

all_logs=$(find . -type f -name "*.log")
num_logs=$(find . -type f -name "*.log" | wc -l)

echo "$all_logs"
echo "Total log files: $num_logs"
