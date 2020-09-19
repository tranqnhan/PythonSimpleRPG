from Source.Weapons.Attacks import *

# Staff - Maximum 2 Moves
class Staff:
    def __init__(self):
        self.name = "Staff"
        self.maximumMoves = 2
        self.attacks = [CastPoison(), Explosion(), Spark()]

# Bow - Maximum 3 Moves
class Bow:
    def __init__(self):
        self.name = "Bow"
        self.maximumMoves = 3
        self.attacks = [QuickShot(), PowerShot(), RainOfArrows()]

# Sword - Maximum 1 Move
class Sword:
    def __init__(self):
        self.name = "Sword"
        self.maximumMoves = 1
        self.attacks = [Strike(), Cut(), Pierce()]