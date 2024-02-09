import Assets.inventory
import Assets.player
import Assets.computer

plyr = Assets.player.Player("Player 1")
print(plyr.inventory)
cmptr = Assets.computer.Computer()
print(cmptr.inventory)