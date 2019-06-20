#!/usr/bin/env bash

file=$1
name=$(basename $file)
bn=${name%.*}
length=$(cat $file | wc -l)
l_train=$(echo "$length * 0.7" |bc|xargs printf "%.0f")
l_dev=$(echo "$length * 0.2" |bc|xargs printf "%.0f")
l_test=$(echo "$length * 0.1" |bc|xargs printf "%.0f")

file_r=$(shuf --random-source=$file $file)
echo "train:" $l_train "dev:" $l_dev "test:" $l_test
echo "$file_r" | head -n $l_train > $bn.train.txt
echo "$file_r" | tail -n +$(( $l_train + 1 ))| head -n $l_dev > $bn.dev.txt
echo "$file_r" | tail -n $l_test > $bn.test.txt


