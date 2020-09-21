from Source.Weapons.Effects import *
import random

# ----- Staff Attacks -----

# CastPoison - Damage: 2 - Hit Chance: 80% - Move Cost: 2 - Induce Poison Affliction
class CastPoison:
    def __init__(self):
        self.name = "Cast Poison"
        self.damage = 2
        self.hitChance = .8
        self.moveCost = 2
        self.effect = Poison(1)

    # Generate an attack
    def attack(self):
        return [self.damage, Poison(1)]

# Explosion - Damage: 10 - Hit Chance: 50% - Move Cost: 2
class Explosion:
    def __init__(self):
        self.name = "Explosion"
        self.damage = 10
        self.hitChance = .5
        self.moveCost = 2
        self.effect = None

    def attack(self):
        return [self.damage, None]

# Spark - Damage: 5 - Hit Chance: 70% - Move Cost: 1
class Spark:
    def __init__(self):
        self.name = "Spark"
        self.damage = 5
        self.hitChance = .7
        self.moveCost = 1
        self.effect = None

    def attack(self):
        return [self.damage, None]

# ----- Bow Attacks -----

# Quick Shot - Damage: 2 - Hit Chance: 90% - Move Cost: 1 - 15% Chance to Induce Bleeding Effect
class QuickShot:
    def __init__(self):
        self.name = "Quick Shot"
        self.damage = 2
        self.hitChance = .9
        self.moveCost = 1
        self.effect = Bleeding(.15)

    def attack(self):
        bleedingEffect = Bleeding(.15)
        if (random.random() <= bleedingEffect.successChance):
            return [self.damage, Bleeding(.15)]
        return [self.damage, None]

# Power Shot - Damage: 12 - Hit Chance: 50% - Move Cost: 2
class PowerShot:
    def __init__(self):
        self.name = "Power Shot"
        self.damage = 12
        self.hitChance = .5
        self.moveCost = 2
        self.effect = None

    def attack(self):
        return [self.damage, None]

# Rain Of Arrows - Damage 7 - Hit Chance: 70% - Move Cost: 3
class RainOfArrows:
    def __init__(self):
        self.name = "Rain Of Arrows"
        self.damage = 7
        self.hitChance = .7
        self.moveCost = 3
        self.effect = None

    def attack(self):
        return [self.damage, None]

# ----- Sword Attacks -----

# Strike - Damage: 10 - Hit Chance: 35% - Move Cost: 1 - 70% Chance to Induce Bleeding Effect
class Strike:
    def __init__(self):
        self.name = "Strike"
        self.damage = 10
        self.hitChance = .35
        self.moveCost = 1
        self.effect = Bleeding(.7)

    def attack(self):
        if (random.random() <= self.effect.successChance):
            return [self.damage, Bleeding(.7)]
        return [self.damage, None]

# Cut - Damage: 5 - Hit Chance: 60% - Move Cost: 1 - 30% Chance to Induce Bleeding Effect
class Cut:
    def __init__(self):
        self.name = "Cut"
        self.damage = 5
        self.hitChance = .6
        self.moveCost = 1
        self.effect = Bleeding(.3)

    def attack(self):
        if (random.random() <= self.effect.successChance):
            return [self.damage, Bleeding(.3)]
        return [self.damage, None]

# Pierce - Damage: 2 - Hit Chance: 100% - Move Cost 1 - 15% Chance to Induce Bleeding Effect
class Pierce:
    def __init__(self):
        self.name = "Pierce"
        self.damage = 2
        self.hitChance = .8
        self.moveCost = 1
        self.effect = Bleeding(.15)

    def attack(self):
        if (random.random() <= self.effect.successChance):
            return [self.damage, Bleeding(.15)]
        return [self.damage, None]