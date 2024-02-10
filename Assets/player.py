import Assets.inventory
import Assets.computer

class Player:
    def __init__(self, name, inventory=None, computer=None, money=None) -> None:
        self.name = name
        self.inventory = inventory
        self.computer = computer
        self.money = money
        if self.money is None:
            self.money = 0
        if self.computer is None:
            self.computer = Assets.computer.Computer()
        if self.inventory is None:
            self.inventory = Assets.inventory.Inventory((5,7))
