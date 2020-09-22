import os
from pathlib import Path
from random import randint

os.system('clear')
playerName = input("Player's name:       ")
charName = input("Character's name:    ")
homePath = str(Path.home())
charPath = str(homePath + '/characters/')
charsReplace = ".,-&'` \\"
stripdblndrsc = "__"
base = (playerName + "_" + charName)
baseURL = "https://www.dndbeyond.com/races/"
raceDB = "Dragonborn"
raceDwf = "Dwarf"
raceElf = "Elf"
raceGnm = "Gnome"
racehHE = "Half-Elf"
raceHalf = "Halfling"
raceHO = "Half-Orc"
raceHmn = "Human"
raceTfl = "Tiefling"
raceAar = "Aarakocra"
raceGen = "Genasi"
raceGol = "Goliath"
speciesList = [raceDB, raceDwf, raceElf, raceGnm, racehHE, raceHalf, raceHO, raceHmn, raceTfl, raceAar, raceGen, raceGol]
speciesList.sort()
NL = '\n'


for list in charsReplace:
    base = base.replace(list, "_")
for list in "__":
    base = base.replace(list, "_")


if not os.path.exists(charPath):
    os.makedirs(charPath)


charFile = open(charPath + base + '.txt', 'w')


def roll_stat():
    stat_roll = []
    count = 0
    while (count < 4):
        rando = randint(1, 6)
        count = count + 1
        stat_roll.append(rando)
    stat_roll.remove(min(stat_roll))
    return sum(stat_roll)


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


def displayStats():
    print(f"The character's Strength is:     ", charStrength)
    print(f"The character's Dexterity is:    ", charDexterity)
    print(f"The character's Constitution is: ", charConstitution)
    print(f"The character's Intelligence is: ", charIntelligence)
    print(f"The character's Wisdom is:       ", charWisdom)
    print(f"The character's Charisma is:     ", charCharisma)


assignStats()
displayStats()
charStats = input("""
Accept as printed.\t\t\t(accept)
Re-assign given values.\t\t\t(assign)
Re-Roll dice. (You get one chance.)\t(reroll)
Input my own.\t\t\t\t(custom)\n\n--> """)
if (charStats == 'accept' or charStats == 'Accept'):
    print(f"Proceeding with species selection.\n")
    rollMethod = "hardcore"
elif (charStats == 'assign' or charStats == 'Assign'):
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
    rollMethod = "custom"
    displayStats()
    print(f"Proceeding with species selection.\n")


def getSpecies():
    global charSpecies
    charSpecies = None
    while (charSpecies not in speciesList):
        charSpecies = input(f"\nChoose your character species from the list below:{NL}{NL.join(sorted(speciesList))}\n: ")
        charSpecies = charSpecies.capitalize()
    return charSpecies


getSpecies()


if rollMethod != "custom":
    if charSpecies == 'Dragonborn':
        charStrength = charStrength + 1
        charCharisma = charCharisma + 1
        print (f"Based on the choice of {charSpecies} as the character species, updated stats are as follows:")
        displayStats()


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
