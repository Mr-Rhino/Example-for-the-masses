#!/bin/ksh
trap 'printf "Thanks for playing.\n\n"' EXIT
#
magicnum=$(($RANDOM%10+1))

print 'Ctrl+c to exit at any time.'
print 'Guess a number between 1 and 10:'
while read guess'?number> '; do
#
if [[ $guess -lt 1 ]]
  then
    printf "\nYou're supposed to choose a number that is greater than 1.\n\n"
elif [[ $guess -gt 10 ]]
  then
    printf "\nYou're supposed to choose a number that is less than 10.\n\n"
elif [[ $guess = $magicnum ]]
  then
    printf "\n$guess is CORRECT!\n\n"
exit
fi
printf "\n$guess is not correct.  :-(\n"
done
