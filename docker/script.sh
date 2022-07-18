#! /bin/bash

filename=$1
output=$2

declare -a top
mapfile -t top < <(tr -c '[:alnum:]' '[\n*]' < $filename | sort | uniq -c | sort -nr | head  -10)
unset top[0]

for i in "${!top[@]}"
do
  echo ${top[$i]}
  name=$(echo ${top[$i]} | tr -d '[:digit:]' | tr -d '[:blank:]')
  touch $output/${name}

done
