def help() -> str:
    return """ Here is a list of commands you can use:

##### On your base :
    help - Shows this message.
    quit - Quits the game.

    inventory - Open your inventory menu.
    computer - Open the computer menu.

    money - Shows your money.
    shop - Open the shop menu.
    buy - Buy something from the shop.
    sell - Sell something from your inventory.

    mission - Open the missions menu.

    return - Returns to the previous menu.

##### When you are in a mission :
    help - Shows this message.
    quit - Quits the game.
    abort - Aborts the mission.

    inventory - Open your inventory menu.
    computer - Open the computer menu.

    << Others commands will be available depending on the mission you are in. >>
    """

def find(command:str) -> str:
    raise NotImplementedError("This function is not implemented yet.")