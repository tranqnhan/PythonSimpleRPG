from Source.GameInfo import gameInfo
from Source.Style import style

# Final Score = Health + Exp + Coins * 2
def displayFinalScore():
    style.displayMessage("title", "Game Over")
    print("\t\nPlayer Name:", gameInfo.player.name)
    print("\tWeapon:", gameInfo.player.weapon.name)
    print("\tArea:", gameInfo.area.name)
    print("\tFinal Health:", gameInfo.player.health)
    print("\tFinal Coins:", gameInfo.player.coins)
    print("\tFinal Experience:", gameInfo.player.exp)
    print("\tFinal Score:", gameInfo.player.health + gameInfo.player.coins * 2 + gameInfo.player.exp)
    print("\nThank you for playing!")