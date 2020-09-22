#!/bin/ksh
# TEST COUNTING DOWN
typeset -i start=$1
typeset -i stop=$2
#
if [[ $# -ne 2 ]]
  then
    printf "\nYou didn't give me two arguments.  This script takes two numbers and counts down from one to the other.\n\n"
    exit
elif [[ ${start} -lt ${stop} ]]
  then
    printf "\n${start} is less than ${stop}.  This script counts down, not up.\n\n"
elif [[ ${start} -eq ${stop} ]]
  then
    print "\n This script counts down from one number to another.  You gave the same number twice.\n"
exit
fi
while [[ ${start} -ge ${stop} ]] ; do
printf  "Counting down: ${start}\n"
start=`expr ${start} - 1`
sleep 1
done
