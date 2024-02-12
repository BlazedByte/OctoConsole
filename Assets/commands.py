import Assets.display as d
import Assets.save

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

def goto_settings(player):
    player.location = "/settings"
    return "You are now in the settings menu."
def change_name(player):
    new_name = d.cinput("What is your new name? > ", d.Fore.WHITE, d.Fore.BLUE)
    player.name = new_name
    return f"Your name has been changed to {new_name}."

def find(command:str,player) -> str:
    commands = {
        "/":{
            "settings":goto_settings,
        },
        "/settings":{
            "change_name":change_name,
        },
    }
    available_commands = commands[player.location]
    for cmd, value in available_commands.items():
        if cmd in command:
            return value(player)
    return "Command not found. Please try again with a valid command."