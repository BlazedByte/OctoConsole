class Inventory:
    def __init__(self, size:tuple=None, items=None) -> None:
        self.items = items
        if self.items is None:
            self.items = [[None for _ in range(size[1])] for _ in range(size[0])]
    def __repr__(self) -> str:
        s = ""
        for row in self.items:
            for item in row:
                if not(item is None):
                    s += f"{item} "
                else:
                    s += "· "
            s += "\n"
        return s[:-1]