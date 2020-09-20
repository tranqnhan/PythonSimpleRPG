from Source.Locations.Enemies import *
from Source.GameInfo import gameInfo
import random

# Village Area
class Village:
    def __init__(self):
        self.name = "Village"
        self.numberOfFights = 0
        self.serialKillerWeight = .4
        self.thiefWeight = .4
        self.banditWeight = .8

    def getEnemy(self):
        self.numberOfFights += 1
        withoutThiefWeight = self.serialKillerWeight + self.banditWeight
        if (gameInfo.player.coins > 0):
           withThiefWeight = withoutThiefWeight + self.thiefWeight
           banditRange = self.banditWeight + self.serialKillerWeight
           roll = random.uniform(0, withThiefWeight)
           if (roll <= self.serialKillerWeight):
               return SerialKiller()
           elif (roll <= banditRange):
               return Bandit()
           else:
               return Thief()
        else:
            roll = random.uniform(0, withoutThiefWeight)
            if (roll <= self.serialKillerWeight):
                return SerialKiller()
            else:
                return Bandit()

    def getBoss(self):
        return CorruptedKnight()