#!/bin/bash

echo "===== SERVER HEALTH ====="
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Date: $(date)"

disk_ok=true
port_ok=true

echo "===== DISK ====="
disk_usage=$(df -h / | tail -n 1 | awk '{print $5}' | sed 's/%//')
if [ "$disk_usage" -lt 50 ]; then
    echo "disk: OK, usage is $disk_usage"
else
    echo "DISK: NOT OK, usage is $disk_usage"
    disk_ok=false
fi
echo "===== NETWORK ====="
if lsof -i :8080 > /dev/null; then
    echo "port 8080 OPEN"
else
    echo "port 8080 NOT OPEN"
    port_ok=false
fi

if [ "$disk_ok" == true ] && [ "$port_ok" == true ]; then
    echo "overall status: HEALTHY"
else
    echo "overall status: UNHEALTHY"
fi