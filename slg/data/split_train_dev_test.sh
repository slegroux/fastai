#!/usr/bin/env bash

file=$1
length=$(cat $file | wc -l)
l_train=$(echo "$length * 0.7" |bc|xargs printf "%.0f")
l_dev=$(echo "$length * 0.2" |bc|xargs printf "%.0f")
l_test=$(echo "$length * 0.1" |bc|xargs printf "%.0f")

echo $l_train, $l_dev, $l_test
