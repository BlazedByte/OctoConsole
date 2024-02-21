import random

def generate_pwd():
    s = ""
    leng = random.randint(6, 15)
    for i in range(leng):
        s += chr(random.randint(33, 126))
    return s

def generate_tree():
    tree = {}
    return tree

class Mission:
    def __init__(self, seed) -> None:
        self.seed = seed
        self.name = hex(seed)[2:]

        self.password = generate_pwd()
        self.completed = False
        self.tree = generate_tree()
    def __repr__(self) -> str:
        return self.name