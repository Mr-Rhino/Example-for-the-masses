import random
from sys import argv

print("Number of arguments: ", len(argv))
print("The arguments are: ", str(argv))

#    This script rolls a user determined set of dice, of various sizes.

# Let's try to catch the possibility of a missing parameter.
try:
    script, die = argv
except ValueError:
    die = "5d6"

try:
    dice, sides = die.split("d")
except ValueError:
    print("Incorrect Values provided. Defaulting to 5d6")
    dice = 5
    sides = 6

die_count = int(dice)
die_type = int(sides)

if not die_count:
    die_count = 4

if not die_type:
    die_type = 6

all_rolls = []

count = 1
while (count < die_count + 1):
    rando = random.randint(1, die_type)
    print(f"Die roll {count}: ", rando)
    count = count + 1
    all_rolls.append(rando)
print()

total = sum(all_rolls)
average = round(float(total / die_count), 2)

print(f"The list of all rolls is:     ", all_rolls)
print(f"The sum of the rolls is:      ", total)
print(f"The average of the rolls is:  ", average)

all_rolls.sort(reverse=True)

print(f"The highest value roll is:    ", all_rolls[0])
print(f"The lowest value roll is:     ", all_rolls[-1])
