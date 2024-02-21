class Mission:
    def __init__(self, seed) -> None:
        self.seed = seed
        self.name = hex(seed)[2:]
    def __repr__(self) -> str:
        return self.name