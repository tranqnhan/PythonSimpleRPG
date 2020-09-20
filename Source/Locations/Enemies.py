# ----- Village Enemies -----

# Thief - Health: 20 - Damage: (2 - 10) - Coin: 20 - Exp: + 2
class Thief:
    def __init__(self):
        self.name = "Thief"
        self.health = 20
        self.minimumDamage = 2
        self.maximumDamage = 10
        self.coinsDrop = 20
        self.expDrop = 2
        self.enemyType = "Steal"

# Bandit - Health: 40 - Damage: (5 - 12) - Coin: 25 - Exp: + 4 
class Bandit:
    def __init__(self):
        self.name = "Bandit"
        self.health = 40
        self.minimumDamage = 5
        self.maximumDamage = 12
        self.coinsDrop = 25
        self.expDrop = 5
        self.enemyType = "Fight"

# Serial Killer - Health: 30  - Damage: (9 - 14) - Coin: 10 - Exp: + 7
class SerialKiller:
    def __init__(self):
        self.name = "Serial Killer"
        self.health = 30
        self.minimumDamage = 9
        self.maximumDamage = 14
        self.coinsDrop = 10
        self.expDrop = 7        
        self.enemyType = "Fight"

# Boss
# Corrupted Knight - Health: 600 - Damage: (10 - 100) - Coin: 50 - Exp: + 20
class CorruptedKnight:
    def __init__(self):
        self.name = "Corrupted Knight"
        self.health = 600
        self.minimumDamage = 10
        self.maximumDamage = 100
        self.coinsDrop = 50
        self.expDrop = 20
        self.appearChance = 0
        self.enemyType = "Fight"

# ----- Mountain Enemies -----

# Salamander - Health: 15 - Damage (2 - 6) - Coins: 5 - Exp: + 2 - Appear Chance Weight: .5
class Salamander:
    def __init__(self):
        self.name = "Salamander"
        self.health = 20
        self.minimumDamage = 2
        self.maximumDamage = 8
        self.coinsDrop = 5
        self.expDrop = 2
        self.enemyType = "Steal"       

# Drake - Health: 30 - Damage (7 - 10) - Coins: 20 - Exp: + 5 - Appear Chance Weight: .5
class Drake:
   def __init__(self):
        self.name = "Drake"
        self.health = 30
        self.minimumDamage = 7
        self.maximumDamage = 10
        self.coinsDrop = 20
        self.expDrop = 5
        self.appearChance = .5
        self.enemyType = "Fight"

# Mountain Lion - Health: 35 - Damage (9 - 15) - Coins: 30 - Exp: + 9 - Appear Chance Weight: .5
class MountainLion:
   def __init__(self):
        self.name = "Mountain Lion"
        self.health = 35
        self.minimumDamage = 9
        self.maximumDamage = 15
        self.coinsDrop = 30
        self.expDrop = 6
        self.appearChance = .5
        self.enemyType = "Fight"

# Boss
# Dragon Queen - Health: 350 - Damage: (40 - 45) - Coin: 50 - Exp: + 20
class DragonQueen:
    def __init__(self):
        self.name = "Dragon Queen"
        self.health = 700
        self.minimumDamage = 40
        self.maximumDamage = 45
        self.coinsDrop = 50
        self.expDrop = 20
        self.appearChance = 0
        self.enemyType = "Fight"

# ----- Forest Enemies -----

# Goblin - Health: 20 - Damage: (5 - 10) - Coins: 5 - Exp: + 2 - Appear Chance Weight: .3
class Goblin:
   def __init__(self):
        self.name = "Goblin"
        self.health = 20
        self.minimumDamage = 5
        self.maximumDamage = 10
        self.coinsDrop = 5
        self.expDrop = 2
        self.enemyType = "Steal"

# Troll - Health: 35 - Damage: (2 - 27) - Coins: 25 - Exp: + 7 - Appear Chance Weight: .7
class Troll:
   def __init__(self):
        self.name = "Troll"
        self.health = 35
        self.minimumDamage = 2
        self.maximumDamage = 27
        self.coinsDrop = 25
        self.expDrop = 7
        self.appearChance = .7
        self.enemyType = "Fight"

# Naga - Health: 60 - Damage: (2 - 15) - Coins: 30 - Exp: + 6 - Appear Chance Weight: .5
class Naga:
   def __init__(self):
        self.name = "Naga"
        self.health = 60
        self.minimumDamage = 2
        self.maximumDamage = 15
        self.coinsDrop = 30
        self.expDrop = 6
        self.appearChance = .5
        self.enemyType = "Fight"

# Boss
# Orc King - Health: 1000 - Damage: (3 - 10) - Coins: 50 - Exp: + 20  
class OrcKing:
    def __init__(self):
        self.name = "Orc King"
        self.health = 1000
        self.minimumDamage = 3
        self.maximumDamage = 10
        self.coinsDrop = 50
        self.expDrop = 20
        self.appearChance = 0
        self.enemyType = "Fight"