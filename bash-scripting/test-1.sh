#!/bin/bash

echo "Hello World"

count=1

if echo hai | grep ha; then
  echo "The condition is true"
else
  echo "The condition is not true"
fi

if (( $count < 10 )); then
  count=$(( $count+1 ))
  echo $count
fi

while (( $count < 10 )); do
  echo $count
  count=$(( $count+1 ))
done


for i in {0..10..5}; do
  echo $i
done > testfile.txt

for i in $@; do
  "$i"
done

args=($@)

array1=(1 2 3 4 5)

echo ${args[0]}

echo ${array1[3]}

while read line; do
  echo $line
done < /dev/stdin