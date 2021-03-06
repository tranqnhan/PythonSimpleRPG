# Event manager decides which event is going to happen next

from Source.Events.ChooseWeaponEvent import ChooseWeaponEvent
from Source.Events.ExploreAreaEvent import ExploreAreaEvent
from Source.Events.StealEvent import StealEvent
from Source.Events.BattleEvent import BattleEvent
from Source.Events.NameEvent import NameEvent

from Source.EventQueue import EventQueue
from Source.Locations.Enemies import *
from Source.GameInfo import gameInfo
from Source.Style import style
from Source.Events.QuizEvent import getRandomQuiz
import random

class EventManager:
    def __init__(self):
        self.eventNumber = 0

    def getNewEvent(self):
        self.eventNumber += 1
        style.displayMessage("title", "Event " + str(self.eventNumber))

        if EventQueue.QUEUE != None:
            temp = EventQueue.QUEUE
            EventQueue.QUEUE = None
            return temp
        elif self.eventNumber == 1:
            return NameEvent()
        elif self.eventNumber == 2:
            return ChooseWeaponEvent()
        elif self.eventNumber == 3:
            return ExploreAreaEvent()
        elif gameInfo.area != None and gameInfo.area.numberOfFights < 9:
            if random.randint(1, 5) == 2:
                return getRandomQuiz()

            if gameInfo.area.numberOfFights < 8:
                enemy = gameInfo.area.getEnemy()
                if enemy.enemyType == "Steal":
                    return StealEvent(enemy)
                elif enemy.enemyType == "Fight":
                    return BattleEvent(enemy)
            else:
                gameInfo.area.numberOfFights += 1
                return BattleEvent(gameInfo.area.getBoss())
        else:
            #No more events
            gameInfo.isEnded = True
            return None

eventManager = EventManager()