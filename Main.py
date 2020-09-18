# This is a game project name Python Simple RPG for Indian Hills Community College's Python class
# 9/17/2020
# Nhan Tran

from GameInfo import gameInfo
from EventManager import eventManager

def main():
    while not gameInfo.isEnded:
        event = eventManager.getNewEvent();
        while not event.isEnded:
            event.displayTurn()
            userInput = input(event.getInputMessage())
            event.processUserInput(userInput)

if __name__ == "Main":
    main()