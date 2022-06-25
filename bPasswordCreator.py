import tkinter.messagebox
from tkinter import *
import os
import sys
import json
from bPassword import addShortcutFromUI, removeShortcutFromUI

win=Tk()
win.title('bPassword')
win.geometry('1200x800')

creationPanel = PanedWindow()
creationPanel.pack(fill=BOTH, expand=1)

abbrivationDir = "C:/Program Files/bPassword"
abbrivationFile = abbrivationDir + "/abrivation_file.json"

abbrevationTabel = []


with open(abbrivationFile, 'r') as openfile:
    unpackedAbbrivationList = json.load(openfile)
for i in unpackedAbbrivationList:
    abbrevationTabel.append(i)

left = Label(creationPanel, text="Creation Panel")

#### Creation Panel ####
creationPanel.add(left)

options = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "`",
    "&",
    "*",
    "?",
    "+",
    "-",
    "`",
    "^"
]

prefix = StringVar()

prefix.set("@")

drop = OptionMenu( creationPanel , prefix , *options )
creationPanel.add(drop)

subShortcutString = StringVar()

shortcutInput = Entry(win, textvariable=subShortcutString)
shortcutInput.insert(0, "example")
creationPanel.add(shortcutInput)

abrValue = StringVar()

abbrationValueInput = Entry(win, textvariable=abrValue)
abbrationValueInput.insert(0, "example")
creationPanel.add(abbrationValueInput)

shortcutOutput=Label(win,text=(prefix.get() + subShortcutString.get() + " -> " + abrValue.get()),width=50,height=30)
creationPanel.add(shortcutOutput)

def showShortcutOutput(*args):
    shortcutOutput.config(text=(prefix.get() + subShortcutString.get() + " -> " + abrValue.get()))

def shortcutCreate():
    abbrevationTabel.append([prefix.get() + subShortcutString.get(), abrValue.get()])
    abbrivationJSONString = json.dumps(abbrevationTabel)
    abbrivationJSON = open(abbrivationFile, "w")
    abbrivationJSON.write(abbrivationJSONString)
    abbrivationJSON.close()
    newAbrevation = []
    newAbrevation.append(prefix.get() + subShortcutString.get())
    newAbrevation.append(abrValue.get())
    addShortcutFromUI(newAbrevation)


createButton = Button(win,text="Create Shortcut", width=10,height=5,command=lambda:[shortcutCreate(), refreshList()])
creationPanel.add(createButton)

subShortcutString.trace("w", showShortcutOutput)
prefix.trace("w", showShortcutOutput)
abrValue.trace("w", showShortcutOutput)
########################

definedPanel = PanedWindow(creationPanel, orient=HORIZONTAL)

creationPanel.add(definedPanel)

top = Label(definedPanel, text="Defined Panel")

#### Defined Panel ####
definedPanel.add(top)

abbervationList = Listbox(definedPanel)
for i in range(len(abbrevationTabel)):
    abbervationList.insert(i + 1, abbrevationTabel[i][0] + " " + abbrevationTabel[i][1])

def refreshList(*args):
    abbervationList.delete(0, len(abbrevationTabel))

    for i in range(len(abbrevationTabel)):
        abbervationList.insert(i + 1, abbrevationTabel[i][0] + " " + abbrevationTabel[i][1])

definedPanel.add(abbervationList)

def deleteEntry():
    selectedEntry = abbervationList.curselection()
    del abbrevationTabel[selectedEntry[0]]
    abbrivationJSONString = json.dumps(abbrevationTabel)
    abbrivationJSON = open(abbrivationFile, "w")
    abbrivationJSON.write(abbrivationJSONString)
    abbrivationJSON.close()
    removeShortcutFromUI(prefix.get() + subShortcutString.get())

deleteButton = Button(win,text="Delete", width=10,height=5,command=lambda:[deleteEntry(), refreshList()])
definedPanel.add(deleteButton)
#######################

win.mainloop()
