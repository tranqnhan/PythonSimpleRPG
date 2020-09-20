# Choose Weapon Event is the first and required event.
# This event askes the user to choose a weapon:
# Sword, Bow, Staff

from Source.Events.BaseEvent import BaseEvent, TurnData
from Source.GameInfo import gameInfo
from Source.Weapons.Weapons import Bow, Sword, Staff
from Source.Style import style

class ChooseWeaponEvent(BaseEvent):
    def __init__(self):
        super().__init__()
        self.chooseWeaponTurnData = TurnData("Choose a weapon", 
                                             "Input a number 1, 2, or 3 to choose a weapon",
                                             ["1. Sword", "2. Bow", "3. Staff"])
        self.currentTurn = self.chooseWeaponTurnData
    
    def displayTurn(self):
        style.displayMessage("title", "Choose Weapon Event")
        style.displayMessage("command", self.chooseWeaponTurnData.eventMessage)
        numberOfOptions = len(self.chooseWeaponTurnData.optionMessages)
        for i in range(0, numberOfOptions):
            style.displayMessage("choice", self.chooseWeaponTurnData.optionMessages[i])
    
    def getInputMessage(self):
        return self.chooseWeaponTurnData.inputMessage

    def processUserInput(self, userInput):
        if (not super().isValidNumber(userInput, 1, len(self.chooseWeaponTurnData.optionMessages))):
            self.chooseWeaponTurnData.inputMessage = "Please enter a valid number 1, 2, or 3"
        else:
            choice = int(userInput)
            if choice == 1:
                gameInfo.player.weapon = Sword()
            elif choice == 2:
                gameInfo.player.weapon = Bow()
            else:
                gameInfo.player.weapon = Staff()
            self.isEnded = True