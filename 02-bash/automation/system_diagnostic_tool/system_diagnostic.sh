#!/bin/bash


echo "===== SYSTEM DIAGNOSTIC ====="

echo "===== SYSTEM ====="

echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Date: $(date)"
disk_ok=true

echo "===== DISK ====="

disk_usage=$(df -h / | tail -n 1 | awk '{print $5}' | sed 's/%//')
if [ "$disk_usage" -le 70 ]; then
    echo "disk usage is $disk_usage, STATUS: OK"
elif [ "$disk_usage" -gt 70 ] && [ "$disk_usage" -le 89 ]; then
    echo "disk usage is $disk_usage, STATUS: WARNING"
else
    echo "disk usage is $disk_usage, STATUS: CRITICAL"
    disk_ok=false
fi

echo "===== PROCESSES ====="
top_processes=$(ps aux | sort -rk 3 | head -n 4)
echo "$top_processes"

echo "===== NETWORK ====="
echo "Port :8080:"
if lsof -i :8080 > /dev/null; then
    echo "port 8080 OPEN"
else
    echo "port 8080 NOT OPEN"
fi

echo "Internet Connectivity:"
if ping -c 1 8.8.8.8 > /dev/null; then
    echo "Internet OK"
else
    echo "Internet FAILED"
fi

echo "DNS Resolution"
if nslookup google.com > /dev/null; then
    echo "DNS: OK"
else
    echo "DNS: FAILED"
fi

echo "===== LOGS ====="
error_count=$(grep -c "ERROR" diagnostic.log)
echo "Errors found: $error_count"

if [ "$error_count" -eq 0 ]; then
    echo "LOGS: OK"
else
    echo "LOGS: $error_count ERRORS FOUND:"
    grep "ERROR" diagnostic.log
fi

echo "===== DIAGNOSTIC SUMMARY ====="

if [ "$disk_ok" = true ]; then
    echo "Disk: OK"
else
    echo "Disk: CRITICAL"
fi

if [ "$error_count" -eq 0 ]; then
    echo "Logs: OK"
else
    echo "Logs: ERRORS FOUND"
fi