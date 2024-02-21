import random

import Assets.display as d
import Assets.mission as mission

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
def help_mission() -> str:
    return help()

# /
def goto_settings(player):
    player.location = "/settings"
    return "You are now in the settings menu."
def goto_inventory(player):
    player.location = "/inventory"
    return f"You are now in the inventory menu.\n{show_inventory(player)}"
def goto_computer(player):
    player.location = "/computer"
    return f"You are now in the computer menu.\n{show_computer(player)}"
def goto_missions(player):
    player.location = "/missions"
    return "You are now in the missions menu."

# /settings
def change_name(player):
    new_name = d.cinput("What is your new name? > ", d.Fore.WHITE, d.Fore.CYAN)
    player.name = new_name
    return f"Your name has been changed to {new_name}."

# /inventory
def show_inventory(player):
    return f"Your inventory:\t{d.format_color_str(str(player.money)+'⚛',d.Fore.YELLOW)}\n{player.inventory}"

# /computer
def show_computer(player):
    return f"Your computer:\n{player.computer.inventory}"

# /missions
def select_mission(player):
    missions_list = [mission.Mission(random.randint(1000000,9999999)) for _ in range(len(player.computer.inventory))]
    s = "Available missions:\n"
    for i, m in enumerate(missions_list):
        s += f"{i} > {m.name}\n"
    d.cprint(s, d.Fore.LIGHTBLUE_EX, 0.01)
    choice = None
    while not(choice in range(len(missions_list))):
        choice = d.cinput("Which mission do you want to take? > ", d.Fore.RESET, d.Fore.CYAN)
        try:
            choice = int(choice)
        except:
            choice = None
    player.mission = missions_list[choice]
    return f"You have taken the mission {player.mission.name}."


def find_cmd(command:str,player) -> str:
    if command == "/":
        player.location = "/"
        return None
    commands = {
        "/":{
            "settings":goto_settings,
            "inventory":goto_inventory,
            "computer":goto_computer,
            "missions":goto_missions,
        },
        "/settings":{
            "change_name":change_name,
        },
        "/inventory":{
            "show":show_inventory,
        },
        "/computer":{
            "show":show_computer,
        },
        "/missions":{
            "select":select_mission
        }
    }
    available_commands = commands[player.location]
    for cmd, value in available_commands.items():
        if cmd in command:
            return value(player)
    return "Command not found. Please try again with a valid command."

def find_cmd_mission(command:str,player) -> str:
    if command == "/":
        player.location = "/"
        return None
    raise NotImplementedError
    if "cd" in command:
        loc = command[3:]
        raise NotImplementedError
        player.location = command[3:]
        return f"You are now in the {player.location} menu."
    return "Command not found. Please try again with a valid command."