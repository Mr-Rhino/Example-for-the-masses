#!/bin/bash
# TEST COUNTING UP
typeset -i start=$1
typeset -i stop=$2
#
if [[ $# -ne 2 ]]
  then
    printf "\n You didn't give me two numbers.  This script takes two numbers and then counts up from one to another.\n\n"
elif [[ ${start} -gt ${stop} ]] 
  then
    printf "\n${stop} is less than ${start}.  This script counts up, not down, so the second number needs to be greater. \n\nDummy.\n\n"
elif [[ ${start} = ${stop} ]]
  then
    printf "\nYou gave me the same number twice.\n\nDummy.\n\n"
exit
fi
#
while [[ ${start} -le ${stop} ]] ; do
echo "Counting up: ${start}"
start=`expr ${start} + 1`
sleep 1
done
