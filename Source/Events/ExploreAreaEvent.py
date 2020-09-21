# Choose Area Event is the second and required event.
# This event askes the user to choose an area to explore:
# Village, Mountain, Forest

from Source.Events.BaseEvent import BaseEvent, TurnData
from Source.GameInfo import gameInfo
from Source.Locations.Areas import Village, Forest, Mountain
from Source.Style import style

class ExploreAreaEvent(BaseEvent):
    def __init__(self):
        super().__init__()
        self.exploreAreaTurnData = TurnData("Explore an area", 
                                             "Input a number to choose an area",
                                             ["1. Village", "2. Forest", "3. Mountain"])
        self.currentTurn = self.exploreAreaTurnData
    
    def displayTurn(self):
        style.displayMessage("title", "Explore An Area Event")
        style.displayMessage("command", self.exploreAreaTurnData.eventMessage)
        numberOfOptions = len(self.exploreAreaTurnData.optionMessages)
        for i in range(0, numberOfOptions):
            style.displayMessage("choice", self.exploreAreaTurnData.optionMessages[i])
    
    def getInputMessage(self):
        return self.exploreAreaTurnData.inputMessage

    def processUserInput(self, userInput):
        if (not super().isValidNumber(userInput, 1, len(self.exploreAreaTurnData.optionMessages))):
            self.exploreAreaTurnData.inputMessage = "Please enter a valid number"
        else:
            choice = int(userInput)
            if choice == 1:
                gameInfo.area = Village()
            elif choice == 2:
                gameInfo.area = Forest()
            else:
                gameInfo.area = Mountain()
            self.isEnded = True