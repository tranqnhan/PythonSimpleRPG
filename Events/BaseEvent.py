# This is a parent base event class for all events. 
# This class should not be created directly.

class BaseEvent:
    def __init__(self):
        self.isEnded = False

    def displayTurn():
        pass

    def getInputMessage():
        pass

    def processUserInput(self, userInput):
        pass

class Turn:
    def __init__(self, numberOfOptions, eventMessage, inputMessage):
        self.numberOfOptions = numberOfOptions
        self.eventMessage = eventMessage
        self.inputMessage = inputMessage

