# Steal event is an event where the player has to pick the correct number to avoid losing coins
# If the player pick the correct number the battle event initiates

from Source.Events.BaseEvent import BaseEvent, TurnData
from Source.Events.BattleEvent import BattleEvent
from Source.GameInfo import gameInfo
from Source.EventQueue import EventQueue
from Source.Style import style
import random

class StealEvent(BaseEvent):
    def __init__(self, enemy):
        super().__init__()
        
        self.maxGuessNumber = random.randint(2, 5)
        self.choice = random.randint(1, self.maxGuessNumber)

        self.enemy = enemy
        self.isSuccess = None
        self.coinLoss = 0

        self.stealEventData = TurnData("A " + enemy.name + " tries to steal your coins!", 
                                       "Guess a number from 1 to " + str(self.maxGuessNumber) + " to catch the " + enemy.name, [])
        self.successEventData = TurnData("You caught the " + enemy.name + "!", 
                                       "Press Enter to continue", [])
        self.failEventData = TurnData("The " + enemy.name + " got away!", 
                                       "Press Enter to continue", [])
        self.currentTurn = self.stealEventData
    
    def displayTurn(self):
        style.displayMessage("title", "Random Stealing Event")
        style.displayMessage("command", self.currentTurn.eventMessage)
        if self.isSuccess != None:
            if not self.isSuccess:
                style.displayMessage("command", "You lost " + str(self.coinLoss) + " coin(s)!")
                style.displayMessage("command", "You have " + str(gameInfo.player.coins) + " coin(s) remaining")
            else:
                style.displayMessage("command", "The " + self.enemy.name + " tries to fight back!")
        print(self.choice)

    def getInputMessage(self):
        return self.currentTurn.inputMessage

    def processUserInput(self, userInput):
        if (self.isSuccess == None):
            if (super().isValidNumber(userInput, 1, self.maxGuessNumber)):
                if (int(userInput) == self.choice):
                    self.isSuccess = True
                    self.currentTurn = self.successEventData
                    EventQueue.QUEUE = BattleEvent(self.enemy)
                else:
                    self.isSuccess = False
                    self.coinLoss = min(random.randint(2, 10), gameInfo.player.coins)
                    gameInfo.player.coins -= self.coinLoss
                    self.currentTurn = self.failEventData
        else:
            self.isEnded = True