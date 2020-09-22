# This script is a D&D Tool belt, intended to provide multiple functions
#import os
#from pathlib import Path
#from random import randint
#import webbrowser
## from sys import argv
## script, action = argv
#
#
#rolld = "Roll dice"
#rolls = "Roll stats"
#openURL = "Open URL"
#avail_actions = [rolld, rolls, openURL]
#
#
## Roll dice
#dice, sides = die.split("d")
#die_count = int(dice)
#die_type = int(sides)
#all_rolls = []
#allowed_dice = [100, 20, 12, 10, 8, 6, 4, 2]
#
#
#def rollem():
#    count = 1
#    while (count < die_count + 1):
#        rando = randint(1, die_type)
##        print(f"Die roll {count}: " "%03d" % rando)
##        print(f"Die roll {count}:  {rando}")
#        print(f"Die roll {count}: ", rando)
#        count = count + 1
#        all_rolls.append(rando)
#
#
#def showresults():
#    total = sum(all_rolls)
#    average = round(float(total / die_count), 2)
#    all_rolls.sort(reverse=True)
#    print(f"The list of all rolls is:     ", all_rolls)
#    print(f"The sum of the rolls is:      ", total)
#    print(f"The average of the rolls is:  ", average)
#    print(f"The highest value roll is:    ", all_rolls[0])
#    print(f"The lowest value roll is:     ", all_rolls[-1])
#
#
#if die_type in allowed_dice:
#    os.system('clear')
#    rollem()
#    showresults()
#else:
##    print(f"That die type is not allowed.  You can choose any die from this list: ", allowed_dice)
#    print(f"That die type is not allowed.  Choose from the following: ", allowed_dice)
#
#
#print()
#
#
#
#
#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
#webbrowser.get("open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome").open("http://"{baseURL}"/"{species})
## Open URL to default browser and view available species.
#baseURL = "https://www.dndbeyond.com/races/"
## I can use these to record player choices, and to append to the baseURL.
#raceDB = "Dragonborn"
#raceDwf = "Dwarf"
#raceElf = "Elf"
#raceGnm = "Gnome"
#raceHE = "Half-Elf"
#raceHalf = "Halfling"
#raceHO = "Half-Orc"
#raceHmn = "Human"
#raceTfl = "Tiefling"
#raceAar = "Aarakocra"
#raceGen = "Genasi"
#raceGol = "Goliath"
#

import dice_roller.py
