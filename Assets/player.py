import Assets.inventory
import Assets.computer

class Player:
    def __init__(self, name, inventory=None, computer=None, money=None) -> None:
        self.name = name
        self.location = "/"
        if money is None:
            self.money = 0
        else:
            self.money = money
        if computer is None:
            self.computer = Assets.computer.Computer()
        else:
            self.computer = Assets.computer.Computer(inventory=Assets.inventory.Inventory(items=computer))
        if inventory is None:
            self.inventory = Assets.inventory.Inventory((5,7))
        else:
            self.inventory = Assets.inventory.Inventory(items=inventory)
        
