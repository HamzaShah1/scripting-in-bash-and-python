#!/bin/bash

current_user=$(whoami)
number_items_in_wd=$(ls | wc -l)
date=$(date)

echo "User: $current_user, Items in directory: $number_items_in_wd, Date: $date"

