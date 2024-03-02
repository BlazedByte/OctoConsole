import random
import datetime

def generate_date(start="1990-01-01", end=datetime.datetime.now().strftime("%Y-%m-%d")):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    result = start + (end - start) * random.random()
    return result.strftime("%Y-%m-%d")

def generate_pwd():
    return "15082023" # The correct code in the tree
    s = ""
    leng = random.randint(6, 15)
    for i in range(leng):
        s += chr(random.randint(33, 126))
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

        self.try_count = 3
    def __repr__(self) -> str:
        return self.name
    
    def try_pwd(self, pwd:str):
        """Try to enter the master password. If the password is incorrect, a message will be printed.

        Parameters
        ----------
        pwd : str
            The password to try

        Returns
        -------
        Bool / None
            True if the password is correct, False if the mission failed, None if the password is incorrect.
        """
        if pwd == self.password:
            self.completed = True
            return True
        self.try_count -= 1
        print("Incorrect password. You have", self.try_count, "tries left.")
        if self.try_count == 0:
            self.completed = True
            return False
        return None