from Source.Events.BaseEvent import BaseEvent
from Source.Style import style
from Source.GameInfo import gameInfo
import random

# This is the QuizData to be inputted into the Quiz Event to process
class QuizData:
    def __init__(self, header, choiceQuestion, choicesList, correctChoice, reward, punishment):
        self.header = header
        self.choiceQuestion = choiceQuestion
        self.choicesList = choicesList
        self.correctChoice = correctChoice
        self.rewardType = reward[0]
        self.punishmentType = punishment[0]
        self.rewardCount = reward[1]
        self.punishmentCount = punishment[1]

class QuizEvent(BaseEvent):
    def __init__(self, quizData):
        super().__init__()
        self.currentTurnData = quizData
        self.inputMessage = "Input a number to choose an option"
        self.state = "Pending"
        
    def displayTurn(self):
        style.displayMessage("title", "Quiz Event")
        
        if self.state == "Pending":
            style.displayMessage("command", self.currentTurnData.header)
            style.displayMessage("command", self.currentTurnData.choiceQuestion)
            numberOfQuestions = len(self.currentTurnData.choicesList) - 1
        
            for i in range(0, numberOfQuestions + 1):
                style.displayMessage("choice", str(i + 1) + ". " + self.currentTurnData.choicesList[i])

        elif self.state == "Win":
            style.displayMessage("command", gameInfo.player.name + " is correct!")
            style.displayMessage("command", gameInfo.player.name + " gained " + str(self.currentTurnData.rewardCount) + " " + self.currentTurnData.rewardType)
            
           
            self.inputMessage = "Press Enter to continue"
            self.isEnded = True
            self.checkPlayerHealth()
        elif self.state == "Lose":
            style.displayMessage("command", gameInfo.player.name + " is wrong!")
            style.displayMessage("command", gameInfo.player.name + " lost " + str(self.currentTurnData.punishmentCount) + " " + self.currentTurnData.punishmentType)
            self.inputMessage = "Press Enter to continue"
            self.isEnded = True
            self.checkPlayerHealth()

    def checkPlayerHealth(self):
        if (gameInfo.player.health <= 0):
            style.displayMessage("command", gameInfo.player.name + " died!")
            gameInfo.isEnded = True

    def getInputMessage(self):
        return self.inputMessage

    def processUserInput(self, userInput):
        if self.state == "Pending":
            choice = userInput
            if (super().isValidNumber(userInput, 1, len(self.currentTurnData.choicesList))):
                choice = int(userInput)
        
            if userInput == self.currentTurnData.correctChoice or choice == self.currentTurnData.correctChoice:
                self.state = "Win"
                if self.currentTurnData.rewardType == "health":
                    gameInfo.player.health += self.currentTurnData.rewardCount
                elif self.currentTurnData.rewardType == "coins":
                    gameInfo.player.coins += self.currentTurnData.rewardCount
            else:
                self.state = "Lose"
                if self.currentTurnData.punishmentType == "health":
                    gameInfo.player.health -= self.currentTurnData.punishmentCount
                elif self.currentTurnData.punishmentType == "coins":
                    gameInfo.player.coins -= self.currentTurnData.punishmentCount

def getRandomQuiz():
    colorQuestion = QuizData("An artist asks you a question: ", "Black or White?", ["Black", "White", "Yellow", "Blue", "USA", "Rainbow"], "yes", ["coins", 10], ["health", 200])
    mathQuestion = QuizData("A mathematician asks you a question: ", "What is the probability that you'll get this question right?", ["25%", "50%", "0%", "25%"], "yes", ["health", 5], ["coins", 30])
    valueQuestion = QuizData("A strange man asks you a question: ", "What do you value more, health or coins?", ["Health", "Coins"], 1, ["coins", -50], ["health", 200])
    whatQuestion = QuizData("What?", "Yes?", ["NO", "No?", "Oh Noooo", "Oh god please no NOOOOO"], "yes", ["health", 1], ["coins", 500])
    failureQuestion = QuizData("The game asks you a question: ", "If you answer this question correctly, do you considered that this is a minor victory, even if you will lose more than you gain?", ["Yes", "No"], 1, ["health", -gameInfo.player.health + 1], ["coins", -gameInfo.player.coins + 1])

    listOfQuizData = [colorQuestion, mathQuestion, valueQuestion, whatQuestion, failureQuestion]
    return QuizEvent(listOfQuizData[random.randint(0, 4)])
