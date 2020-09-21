# This is a game project name Python Simple RPG for Indian Hills Community College's Python class
# Nhan Tran
# 9/17/2020


# Developer Note: 
# Run Windows Command Prompt, 
# navigate to the location where Main.py file is stored, 
# and then type in the Command Prompt "python Main.py" for better format! 

# It works in Visual Studio but for some reason the colors did not show up.

from Source.GameInfo import gameInfo
from Source.EventManager import eventManager
from Source.FinalScore import displayFinalScore
from Source.Style import style
import os

def main():
    while not gameInfo.isEnded:
        event = eventManager.getNewEvent();
        if event != None:
            while not event.isEnded:
                event.displayTurn()
                userInput = input(style.displayMessage("input", event.getInputMessage()))
                event.processUserInput(userInput)
                os.system("cls")
        else:
            os.system("cls")
            break
        os.system("cls")
    displayFinalScore()

os.system("cls")
main()