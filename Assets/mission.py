import Assets.mission_generation as generation

class Mission:
    def __init__(self, id) -> None:
        # self.seed = id
        self.name = hex(id)[2:]
        self.completed = False

        self.password, self.tree = generation.generate_mission()
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