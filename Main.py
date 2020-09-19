# This is a game project name Python Simple RPG for Indian Hills Community College's Python class
# 9/17/2020
# Nhan Tran

from Source.GameInfo import gameInfo
from Source.EventManager import eventManager
from Source.FinalScore import displayFinalScore
from Source.Style import style
import os

def main():
    while not gameInfo.isEnded:
        event = eventManager.getNewEvent();
        while not event.isEnded:
            event.displayTurn()
            userInput = input(style.displayMessage("input", event.getInputMessage()))
            event.processUserInput(userInput)
            os.system("cls")
    displayFinalScore()

os.system("cls")
main()