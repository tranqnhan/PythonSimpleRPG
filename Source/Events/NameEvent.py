from Source.Events.BaseEvent import BaseEvent, TurnData
from Source.GameInfo import gameInfo
from Source.Style import style

class NameEvent(BaseEvent):
    def __init__(self):
        super().__init__()
        self.nameTurnData = TurnData("What is your name?", 
                                    "Input your name here", [])
        self.currentTurn = self.nameTurnData
    
    def displayTurn(self):
        style.displayMessage("title", "Name Event")
        style.displayMessage("command", self.nameTurnData.eventMessage)
    
    def getInputMessage(self):
        return self.nameTurnData.inputMessage

    def processUserInput(self, userInput):
        input = userInput.strip()
        if (input != ""):
            gameInfo.player.name = input
        self.isEnded = True

