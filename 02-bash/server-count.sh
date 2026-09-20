#!/bin/bash

unique_servers=$(sort $1 | uniq -c)
echo "$unique_servers"