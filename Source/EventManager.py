from Source.Events.ChooseWeaponEvent import ChooseWeaponEvent
from Source.Style import style

class EventManager:
    def __init__(self):
        self.eventNumber = 0

    def getNewEvent(self):
        self.eventNumber += 1
        style.displayMessage("title", "Event " + str(self.eventNumber))
        return ChooseWeaponEvent()

eventManager = EventManager()