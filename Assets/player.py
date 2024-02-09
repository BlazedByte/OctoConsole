import Assets.inventory

class Player:
    def __init__(self, name, inventory=None) -> None:
        self.name = name
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = Assets.inventory.Inventory((5,7))
