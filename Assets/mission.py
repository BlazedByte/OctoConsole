import random

def generate_pwd():
    s = ""
    leng = random.randint(6, 15)
    for i in range(leng):
        s += chr(random.randint(33, 126))
    return "15082023" # The correct code in the tree
    return s

def generate_tree():
    tree = {
        "private":{
            "holidays":"I went to london : 2023-08-15,\nto paris : 2022-07-01,\nto new-york : 2021-06-15;\nI love travelling !",
            "passwords":{
                "administrator":"The new password is the date of my last holiday ! (ddmmyyyy)",
                "my-phone":"The password of my phone is : 123456"
            }
        }
    }
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