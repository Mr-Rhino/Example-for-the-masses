# This script creates a D&D 5e character either interactively, or randomly
# from sys import argv
# script, die = argv
import os
from pathlib import Path
from random import randint

# Start with clearing the screen, get the Player's name, and then the Character's name
os.system('clear')
playerName = input("Player's name:       ")
charName = input("Character's name:    ")
# Need to establish a location for the record file.  Can I do this the same way in Windows machines?
homePath = str(Path.home())
charPath = str(homePath + '/characters/')
# Users might have crazy characters in their character names.  Start recording keyboard
# characters that I will need to strip out.
charsReplace = ".,-&'` \\"
base = (playerName + "_" + charName)
# I'd like for users to be able to look up their character species.  Give them
# a URL to the player character species.
baseURL = "https://www.dndbeyond.com/races/"
# I can use these to record player choices, and to append to the baseURL.
raceDB = "Dragonborn"
raceDwf = "Dwarf"
raceElf = "Elf"
raceGnm = "Gnome"
raceHE = "Half-Elf"
raceHalf = "Halfling"
raceHO = "Half-Orc"
raceHmn = "Human"
raceTfl = "Tiefling"
raceAar = "Aarakocra"
raceGen = "Genasi"
raceGol = "Goliath"
# Start a list of all available species, and then sort it.
speciesList = [raceDB, raceDwf, raceElf, raceGnm, raceHE, raceHalf, raceHO, raceHmn, raceTfl, raceAar, raceGen, raceGol]
speciesList.sort()
# I needed this in order to get what I wanted out of the getSpecies function.  Better ways?


# Sub-species and variants
# Dragon
DBblack = "Black"
DBblue = "Blue"
DBbrass = "Brass"
DBbronze = "Bronze"
DBcopper = "Copper"
DBgold = "Gold"
DBgreen = "Green"
DBred = "Red"
DBsilver = "Silver"
DBwhite = "White"
# Dwarf
DwfHill = "Hill"
DwfMt = "Mountain"
# Elf
ElfHigh = "High"
ElfWood = "Wood"
ElfDark = "Dark"
# Gnome
GnmDeep = "Deep"
GnmScribe = "Scribing"
GnmRock = "Rock"
# Half-Elf
# Halfling
# Half-Orc
# Human
# Tiefling
# Aarakocra
# Genasi
# Goliath


NL = '\n'


# Clean up the keyboard characters provided by weird players.
for list in charsReplace:
    base = base.replace(list, "_")
for list in "__":
    base = base.replace(list, "_")


# Make the user's record directory.
if not os.path.exists(charPath):
    os.makedirs(charPath)


# Python opens a file instead of re-directs output like Bash.  Open file for write.
charFile = open(charPath + base + '.txt', 'w')


# Define function for rolling stats.
# Should I re-write to take input on number of dice sides?
# Can I make my own library?   Requires learning C, I think.
# Does someone else have a D&D library?
# Roll 4 dice, drop the lowest.  I'm a softie.
def roll_stat():
    stat_roll = []
    count = 0
    while (count < 4):
        rando = randint(1, 6)
        count = count + 1
        stat_roll.append(rando)
    stat_roll.remove(min(stat_roll))
    return sum(stat_roll)


# Assign stats, leverage the roll_stat function.
# Since I turned this into the assignStats function, and wanted to get data OUT of it
# I had to assign my stat variables as global.  Otherwise I wasn't able to get other functions to use them.
# I'm not sure that I need to use the return command now that variables are global.  Test this.
def assignStats():
    global charStrength, charDexterity, charConstitution, charIntelligence, charWisdom, charCharisma, all_rolls
    charStrength = roll_stat()
    charDexterity = roll_stat()
    charConstitution = roll_stat()
    charIntelligence = roll_stat()
    charWisdom = roll_stat()
    charCharisma = roll_stat()
    all_rolls = [charStrength, charDexterity, charConstitution, charIntelligence, charWisdom, charCharisma]
    all_rolls.sort(reverse=True)
    return charStrength
    return charDexterity
    return charConstitution
    return charIntelligence
    return charWisdom
    return charCharisma


# Create function displayStats.  Was repeating the same print lines too many times.
def displayStats():
    print(f"The character's Strength is:     ", charStrength)
    print(f"The character's Dexterity is:    ", charDexterity)
    print(f"The character's Constitution is: ", charConstitution)
    print(f"The character's Intelligence is: ", charIntelligence)
    print(f"The character's Wisdom is:       ", charWisdom)
    print(f"The character's Charisma is:     ", charCharisma)


# Assign and then display the character stats.
assignStats()
displayStats()
# Let the player/user reassign stats if he/she wants to.
# Also let the user input own stats.  If this script is good enough, someone
# may use it to record existing characters.
# Only let the user re-roll one time.  Let's not waste time re-rolling over and
# over.  Sometime bad stats make the game more fun.
charStats = input("""
Accept as printed.\t\t\t(accept)
Re-assign given values.\t\t\t(assign)
Re-Roll dice. (You get one chance.)\t(reroll)
Input my own.\t\t\t\t(custom)\n\n--> """)
if (charStats == 'accept' or charStats == 'Accept'):
    print(f"Proceeding with species selection.\n")
    rollMethod = "hardcore"
elif (charStats == 'assign' or charStats == 'Assign'):
    # It is a lot easier to remove the requested stat from the list, instead of relying on honesty.
    os.system('clear')
    charStrength = input(f"Specify the character attribute Strength from available values:\n\t{all_rolls} : ")
    all_rolls.remove(int(charStrength))
    charDexterity = input(f"Specify the character attribute Dexterity from remaining values:\n\t{all_rolls} : ")
    all_rolls.remove(int(charDexterity))
    charConstitution = input(f"Specify the character attribute Constitution from remaining values:\n\t{all_rolls} : ")
    all_rolls.remove(int(charConstitution))
    charIntelligence = input(f"Specify the character attribute Intelligence from remaining values:\n\t{all_rolls} : ")
    all_rolls.remove(int(charIntelligence))
    charWisdom = input(f"Specify the character attribute Wisdom from remaining values:\n\t{all_rolls} : ")
    all_rolls.remove(int(charWisdom))
    charCharisma = int(sum(all_rolls))
    print(f"You chose to assign the following stats.",)
    rollMethod = "manualAssign"
    displayStats()
    print(f"Proceeding with species selection.\n")
elif (charStats == 'reroll' or charStats == 'Reroll'):
    del all_rolls
    assignStats()
    print(f"Your one re-roll resulted in the following stats.",)
    rollMethod = "reroll"
    displayStats()
    print(f"Proceeding with species selection.\n")
else:
    del all_rolls
    charStrength = input(f"Specify the character attribute Strength:     ")
    charDexterity = input(f"Specify the character attribute Dexterity:    ")
    charConstitution = input(f"Specify the character attribute Constitution: ")
    charIntelligence = input(f"Specify the character attribute Intelligence: ")
    charWisdom = input(f"Specify the character attribute Wisdom:       ")
    charCharisma = input(f"Specify the character attribute Charisma:     ")
    print(f"You assigned the following stats.")
    # Add the rollMethod variable.  If people have pre-existing characters,
    # do not bump up their stats.  Should already have been taken care of.
    rollMethod = "custom"
    displayStats()
    print(f"Proceeding with species selection.\n")


def getSpecies():
    global charSpecies
    charSpecies = None
    # How do I get some good output to let the user have access to the
    # character species URL if they need it?  Started here, but took it out.
    # Looked too messy.
    # for list in speciesList:
    #     print(f"{baseURL}{list}")
    while (charSpecies not in speciesList):
        charSpecies = input(f"\nChoose your character species from the list below:{NL}{NL.join(sorted(speciesList))}\n: ")
        # The URL isn't case-sensitive, but Python variable value matching is.
        # set to proper case.
        # Originally used the ".capitalize" method, found that species with hyphens stopped matching.
        # resolve by switching to ".title" method.
        charSpecies = charSpecies.title()
    return charSpecies

# Can I manage the above updates via a dictionary?
# Looks messy at first, but could be easier in the long run.
# 1 to 1 relationship between key and value pairs.
# updateStatsforSpecies = dict ([
# (raceDBstr, 2),
# (raceDBcha, 1),
# ])

# function getSpecies only operates once.  Does that need a function,
# or should I take it out of the function?
getSpecies()


# Don't let "custom" rollMethod value update stats.  should already be
# accounted for.  Will need to track that later and have a level function
# for the "custom" rollMethod characters
if rollMethod != "custom":
    if charSpecies == 'Dragonborn':
        charStrength = charStrength + 1
        charCharisma = charCharisma + 1
        print (f"Based on the choice of {charSpecies} as the character species, updated stats are as follows:")
        displayStats()
    # Commented out Dwarf section for testing.  So far, so good.
#    elif charSpecies == 'Dwarf':
#        charConstitution = charConstitution + 1
#        print(f"Dwarves have two optional sub-races: {}")


# Write out the Player and character information, then close the file.
# Can and should I try to pad integers with leading zeroes?
# Might help single and double digit character stats looking pretty.
# Test with output file.
charFile.write(f"Player's name:    {playerName}\n\n")
charFile.write(f"Character name:   {charName}\t\t\tCharacter species:   {charSpecies}\n")
charFile.write(f"Strength:         {charStrength}\n")
charFile.write(f"Dexterity:        {charDexterity}\n")
charFile.write(f"Constitution:     {charConstitution}\n")
charFile.write(f"Intelligence:     {charIntelligence}\n")
charFile.write(f"Wisdom:           {charWisdom}\n")
charFile.write(f"Charisma:         {charCharisma}\n")
charFile.write("\n")
charFile.close()


# Can I start working through a way to get a URL list upon demand?
# Ideally this would get inserted into the getSpecies function
# for list in speciesList:
#     print(f"{list}\t\t{baseURL}{list}")
