from Source.Player import Player

class GameInfo:
    def __init__(self):
        self.isEnded = False
        self.area = None
        self.player = Player()

gameInfo = GameInfo()