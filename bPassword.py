from email import message
from turtle import title
import keyboard
import os
import json
import subprocess



abbrivationDir = "C:/Program Files/bPassword"
abbrivationFile = abbrivationDir + "/abrivation_file.json"


dirExist = os.path.exists(abbrivationDir)
fileExist = os.path.exists(abbrivationFile)

abbrivationTabel = []

def main():

    if not dirExist:
        os.makedirs(abbrivationDir)
        file = open(abbrivationFile, "x")
        file.close()
    elif not fileExist:
        file = open(abbrivationFile, "x")
        file.close()
    else:
        try:
            with open(abbrivationFile, 'r') as openfile:
                unpackedAbbrivationList = json.load(openfile)
                for i in unpackedAbbrivationList:
                    abbrivationTabel.append(i)
                for i in range(len(abbrivationTabel)):
                    keyboard.add_abbreviation(abbrivationTabel[i][0], abbrivationTabel[i][1])
        except FileNotFoundError:
            pass
    keyboard.wait()

def addShortcutFromUI(shortcutTable):
    keyboard.add_abbreviation(shortcutTable[0], shortcutTable[1])

def removeShortcutFromUI(abbrevationToRemove):
    keyboard.remove_abbreviation(abbrevationToRemove)

if __name__ == "__main__":
    main()

##keyboard.add_abbreviation("@e", "ClaytonStout1@gmail.com")
##keyboard.add_abbreviation("@su", "Claytonfox1")
##keyboard.add_abbreviation("@asu", "Sweaty_Nerd911")
##keyboard.add_abbreviation("@vu", "TheRealBloody45")
##keyboard.add_abbreviation("@p", "Louiedog2012")
##keyboard.add_abbreviation("@di", "https://discord.gg/FktDeFUPe8")
