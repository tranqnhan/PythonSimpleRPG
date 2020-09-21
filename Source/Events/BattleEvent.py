# Battle Event is the main event
# This event simulate a battle between the enemy and the player
# The battle between any enemies is random based on the area chosen
# The boss enemy battle always come after 8 consecutive fights

from Source.Events.BaseEvent import BaseEvent, TurnData
from Source.GameInfo import gameInfo
from Source.Style import style
import random

class BattleEvent(BaseEvent):
    def __init__(self, enemy):
        super().__init__()

        self.enemy = enemy
        self.gain = {"Health": self.enemy.health // 2, "Coins": self.enemy.coinsDrop, "Exp": self.enemy.expDrop}

        self.enemyCastEffect = None
        self.playerWeapon = gameInfo.player.weapon
        self.currentNumberOfMoves = self.playerWeapon.maximumMoves

        self.fightData = TurnData( self.getEnemyStatus() , 
                                   "Input a number to choose an attack",
                                   ["1. " + self.getAttackStatus(self.playerWeapon.attacks[0]), 
                                    "2. " + self.getAttackStatus(self.playerWeapon.attacks[1]), 
                                    "3. " + self.getAttackStatus(self.playerWeapon.attacks[2])])
        self.hitData = TurnData ("", "Press Enter to continue", [])

        self.state = "DisplayBattle"
        self.currentTurn = self.fightData
        self.playerTurn = True
        self.previousTurnHit = {"Attacker" : gameInfo.player.name, "Defender" : self.enemy.name, "Damage" : 0, "Effect": None, "Miss" : False}

    def displayTurn(self):
        style.displayMessage("title", "Battle Event")

        if self.state == "DisplayBattle":
            self.currentTurn = self.fightData
            self.displayBattle()
        elif self.state == "DisplayHit":
            self.currentTurn = self.hitData
            self.displayHit()
            self.processEnemyEffect()
        elif self.state == "DisplayWinner":
            self.signalEndBattleEvent()

    def getInputMessage(self):
        return self.currentTurn.inputMessage

    def processUserInput(self, userInput):
        if self.enemy.health == 0 or gameInfo.player.health == 0:
            self.state = "DisplayWinner"
        elif not self.playerTurn and self.state == "DisplayHit":
            self.enemyFightTurn()
            self.playerTurn = True
            self.currentNumberOfMoves = self.playerWeapon.maximumMoves
        elif self.playerTurn and self.state == "DisplayHit":
            self.state = "DisplayBattle"
        elif self.playerTurn and self.state == "DisplayBattle":
           self.playerFightTurn(userInput)

    def enemyFightTurn(self):
        self.previousTurnHit["Attacker"] = self.enemy.name
        self.previousTurnHit["Defender"] = gameInfo.player.name
        damage = random.randint(self.enemy.minimumDamage, self.enemy.maximumDamage)
        gameInfo.player.health = max(gameInfo.player.health - damage, 0)
        self.previousTurnHit["Damage"] = damage
        self.previousTurnHit["Effect"] = None
        self.previousTurnHit["Miss"] = False
        self.state = "DisplayHit"

    def processEnemyEffect(self):
        if self.enemyCastEffect != None:
            if self.enemyCastEffect.turnRemaining > 0:
                self.enemyCastEffect.turnRemaining -= 1
                damage = self.enemyCastEffect.damage
                self.enemy.health = max(self.enemy.health - damage, 0)
                style.displayMessage("command", "{} took {} damage because of the {}!".format(self.enemy.name, damage, self.enemyCastEffect.name))
            else:
                self.enemyCastEffect = None

    def playerFightTurn(self, userInput):
        if (not super().isValidNumber(userInput, 1, len(self.currentTurn.optionMessages))):
            self.fightData.inputMessage = "Please enter a valid number"
        else:
            choice = int(userInput) - 1
            att = self.playerWeapon.attacks[choice]
            if att.moveCost <= self.currentNumberOfMoves:
                self.previousTurnHit["Attacker"] = gameInfo.player.name
                self.previousTurnHit["Defender"] = self.enemy.name
                
                roll = 1 if att.hitChance == 1 else random.random()
                if roll <= att.hitChance:
                    self.previousTurnHit["Miss"] = False
                    damage = att.attack()
                    modifedDamage = gameInfo.player.exp + damage[0]
                    self.previousTurnHit["Damage"] = modifedDamage
                    if damage[1] != None:
                        self.enemyCastEffect = damage[1]
                        self.previousTurnHit["Effect"] = damage[1].name
                    else:
                        self.previousTurnHit["Effect"] = None
                    self.enemy.health = max(self.enemy.health - modifedDamage, 0)
                else:
                    self.previousTurnHit["Miss"] = True

                self.currentNumberOfMoves -= att.moveCost
                self.state = "DisplayHit"

            if self.currentNumberOfMoves <= 0:
                self.playerTurn = False
            
            self.fightData.inputMessage = "Input a number to choose an attack that is <= the move cost remaining" 
        
    def signalEndBattleEvent(self):
        self.currentTurn = self.hitData
        if self.enemy.health <= 0:
            style.displayMessage("command", "{} died!".format(self.enemy.name))
            style.displayMessage("command",  gameInfo.player.name + " gained {} health, {} coins, and {} experience!".format(self.gain["Health"], self.gain["Coins"], self.gain["Exp"]))
            player = gameInfo.player
            player.health += self.gain["Health"]
            player.coins += self.gain["Coins"]
            player.exp += self.gain["Exp"]
        else:
            style.displayMessage("command", gameInfo.player.name + " died!")
            gameInfo.isEnded = True
        self.isEnded = True

    def displayBattle(self):
        if (self.turnNumber == 0):
            style.displayMessage("command", gameInfo.player.name + " have encountered a " + self.enemy.name)
        self.fightData.eventMessage = self.getEnemyStatus()
        style.displayMessage("command", self.fightData.eventMessage)
        numberOfOptions = len(self.fightData.optionMessages)
        for i in range(0, numberOfOptions):
            style.displayMessage("choice", self.fightData.optionMessages[i])
        style.displayMessage("command", self.getPlayerStatus())

    def displayHit(self):
        message = "{} attacks {}. ".format(self.previousTurnHit["Attacker"], self.previousTurnHit["Defender"])
        if not self.previousTurnHit["Miss"]:
            message += "{} loses {} health! ".format(self.previousTurnHit["Defender"], self.previousTurnHit["Damage"])
            if self.previousTurnHit["Effect"] != None:
                message += "{} got {}!".format(self.previousTurnHit["Defender"], self.previousTurnHit["Effect"])
        else:
            message += "{} missed!".format(self.previousTurnHit["Attacker"])
        style.displayMessage("command", message)

    def getPlayerStatus(self):
        player = gameInfo.player
        return "{}: [Health: {}] [Moves Remaining: {}]".format(player.name, player.health, self.currentNumberOfMoves)

    def getAttackStatus(self, att):
        player = gameInfo.player
        if (att.effect == None):
            return "{}: \n\t\t[Damage: {}] \n\t\t[Hit Chance: {}%] \n\t\t[Move Cost: {}]".format(att.name, player.exp + att.damage, att.hitChance * 100, att.moveCost)
        return "{}: \n\t\t[Damage: {}] \n\t\t[Hit Chance: {}%] \n\t\t[Move Cost: {}] \n\t\t[Effect: {}] \n\t\t[Effect Cast Chance: {}%]".format(att.name,  player.exp + att.damage, att.hitChance * 100, att.moveCost, att.effect.name, att.effect.successChance * 100)

    def getEnemyStatus(self):
        return "{}: [Health: {}] [Min Damage: {}] [Max Damage: {}]".format(self.enemy.name, self.enemy.health, self.enemy.minimumDamage, self.enemy.maximumDamage)