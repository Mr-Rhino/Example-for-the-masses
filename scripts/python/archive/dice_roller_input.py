# This script rolls a determined set of dice, of various sizes.
# import os
# from random import randint
# from sys import argv
# script, die = argv
#
# dice, sides = die.split("d")
# die_count = int(dice)
# die_type = int(sides)
# all_rolls = []
# allowed_dice = [100, 20, 12, 10, 8, 6, 4, 2]
#
#
# def rollem():
#     count = 1
#     while (count < die_count + 1):
#         rando = randint(1, die_type)
#         print(f"Die roll {count}: ", rando)
#         count = count + 1
#         all_rolls.append(rando)
#
#
# def showresults():
#     total = sum(all_rolls)
#     average = round(float(total / die_count), 2)
#     all_rolls.sort(reverse=True)
#     print(f"The list of all rolls is:     ", all_rolls)
#     print(f"The sum of the rolls is:      ", total)
#     print(f"The average of the rolls is:  ", average)
#     print(f"The highest value roll is:    ", all_rolls[0])
#     print(f"The lowest value roll is:     ", all_rolls[-1])
#
#
# if die_type in allowed_dice:
#     os.system('clear')
#     rollem()
#     showresults()
# else:
#     print(f"That die type is not allowed.  You can choose any die from this list: ", allowed_dice)
#
#
# print()
#
# This script rolls a determined set of dice, of various sizes.
import os
from random import randint
#from sys import argv
#script, die = argv


die = input("Specify roll in format like '3d6' in order to receive results: ")


dice, sides = die.split("d")
die_count = int(dice)
die_type = int(sides)
all_rolls = []
allowed_dice = [100, 20, 12, 10, 8, 6, 4, 2]


def rollem():
    count = 1
    while (count < die_count + 1):
        rando = randint(1, die_type)
        print(f"Die roll {count}: ", rando)
        count = count + 1
        all_rolls.append(rando)


def showresults():
    total = sum(all_rolls)
    average = round(float(total / die_count), 2)
    all_rolls.sort(reverse=True)
    print(f"The list of all rolls is:     ", all_rolls)
    print(f"The sum of the rolls is:      ", total)
    print(f"The average of the rolls is:  ", average)
    print(f"The highest value roll is:    ", all_rolls[0])
    print(f"The lowest value roll is:     ", all_rolls[-1])


if die_type in allowed_dice:
    os.system('clear')
    rollem()
    showresults()
else:
    print(f"That die type is not allowed.  You can choose any die from this list: ", allowed_dice)
