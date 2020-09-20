# Style the messages with consistent styling
class Style:
    def __init__(self):
        self.color = {
            "PURPLE" : '\033[95m',
            "CYAN" : '\033[96m',
            "DARKCYAN" : '\033[36m',
            "BLUE" : '\033[94m',
            "GREEN" : '\033[92m',
            "YELLOW" : '\033[93m',
            "RED" : '\033[91m',
            "BOLD" : '\033[1m',
            "UNDERLINE" : '\033[4m',
            "END" : '\033[0m',
        }
        self.TITLE_WIDTH = 40

    def displayMessage(self, type, message):
        if type == "title":
            numberOfCharacters = message
            leftOver = self.TITLE_WIDTH - len(message)
            distribute = leftOver // 2
            leftSide = "-" * distribute
            rightSide = "-" * distribute + "-" * (leftOver % 2)

            newMessage = leftSide + " " + message + " " + rightSide
            print(self.color["BOLD"] + self.color["PURPLE"] + newMessage + self.color["END"])
        elif type == "choice":
            newMessage = "\t" + message
            print(newMessage)
        elif type == "input":
            newMessage = " :: " + message + " > "
            return self.color["GREEN"] + newMessage + self.color["END"]
        elif type == "command":
            newMessage = " > " + message
            print(self.color["CYAN"] + newMessage + self.color["END"])
        else:
            print(message)

style = Style()