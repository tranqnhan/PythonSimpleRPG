# This is a parent base event class for all events. 
# This class should not be created directly.

class BaseEvent:
    def __init__(self):
        self.isEnded = False
        self.turnNumber = 0
        self.currentTurn = None

    def displayTurn(self):
        print("No display turn implemented!")

    def getInputMessage(self):
        print("No input message implemented!")

    def processUserInput(self, userInput):
        print("No process implemented!")

        
    # This method tries to check whether the userInput is a valid integer input.
    # The inherited method should call this method to check the userInput.
    # Return true if input is a valid input, false otherwise.
    def isValidNumber(self, userInput, min, max):
        try:
            int(userInput)
        except ValueError:
            return False
        number = int(userInput)

        return number >= min and number <= max

#Storing a single turn display data
class TurnData:
    def __init__(self, eventMessage, inputMessage, optionMessages):
        self.optionMessages = optionMessages
        self.eventMessage = eventMessage
        self.inputMessage = inputMessage

