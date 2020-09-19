# Poison effect - 2 damage per turn for 5 turns
class Poison:
    def __init__(self, successChance):
        self.name = "Poison Effect"
        self.successChance = successChance
        self.turnRemaining = 5
        self.damage = 2

# Bleeding effect - 4 damage per turn for 3 turns
class Bleeding:
    def __init__(self, successChance):
        self.name = "Bleeding Effect"
        self.successChance = successChance
        self.turnRemaining = 3
        self.damage = 4