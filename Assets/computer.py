import Assets.inventory

class Computer:
    def __init__(self, inventory=None) -> None:
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = Assets.inventory.Inventory((2,3))