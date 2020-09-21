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

# Mountain Area
class Mountain:
    def __init__(self):
        self.name = "Mountain"
        self.numberOfFights = 0
        self.drakeWeight = .5
        self.salamanderWeight = .5
        self.mountainLionWeight = .5

    def getEnemy(self):
        self.numberOfFights += 1
        withoutSalamanderWeight = self.drakeWeight + self.mountainLionWeight
        if (gameInfo.player.coins > 0):
           withSalamanderWeight = withoutSalamanderWeight + self.salamanderWeight
           mountainLionRange = self.mountainLionWeight + self.drakeWeight
           roll = random.uniform(0, withSalamanderWeight)
           if (roll <= self.drakeWeight):
               return Drake()
           elif (roll <= mountainLionRange):
               return MountainLion()
           else:
               return Salamander()
        else:
            roll = random.uniform(0, withoutSalamanderWeight)
            if (roll <= self.drakeWeight):
                return Drake()
            else:
                return MountainLion()

    def getBoss(self):
        return DragonQueen()

# Forest Area
class Forest:
    def __init__(self):
        self.name = "Forest"
        self.numberOfFights = 0
        self.goblinWeight = .3
        self.trollWeight = .7
        self.nagaWeight = .5

    def getEnemy(self):
        self.numberOfFights += 1
        withoutGoblinWeight = self.trollWeight + self.nagaWeight
        if (gameInfo.player.coins > 0):
           withGoblinWeight = withoutGoblinWeight + self.goblinWeight
           nagaRange = self.trollWeight + self.nagaWeight
           roll = random.uniform(0, withGoblinWeight)
           if (roll <= self.trollWeight):
               return Troll()
           elif (roll <= nagaRange):
               return Naga()
           else:
               return Goblin()
        else:
            roll = random.uniform(0, withoutGoblinWeight)
            if (roll <= self.trollWeight):
                return Troll()
            else:
                return Naga()

    def getBoss(self):
        return OrcKing()