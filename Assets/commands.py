import random

import Assets.display as d
import Assets.mission as mission

def help() -> str:
    return """ Here is a list of commands you can use:
    help - Shows this message.
    quit - Quits the game.

    inventory - Open your inventory menu.
        In the inventory menu:
            show - Shows your inventory and your money
    computer - Open the computer menu.
        In the computer menu:
            show - Shows your computer inventory.
    missions - Open the missions menu.
        In the missions menu:
            select - Select a mission to take.
    settings - Open the settings menu.
        In the settings menu:
            change_name - Change your name.
    / - Go back to the main menu."""
def help_mission() -> str:
    return """Here is a list of commands you can use:
    help - Shows this message.
    quit - Quits the game.
    abort - Aborts the mission.

    try <password> - Try to enter the master password to complete the mission.
    ls - List the files and folders in the current location.
    cat <file> - Show the content of a file.
    cd <folder> - Go to a folder.
    cd .. - Go back to the parent folder.
    / - Go back to the main folder."""

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
    player.location = "/"
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
    if "abort" in command:
        if d.cinput("Are you sure? y/n > ", d.Fore.RED) in ["y","yes","Y","YES"]:
            player.mission = None
            player.location = "/"
            return "You have aborted the mission."
    if command.startswith("try "):
        pwd = command[4:]
        r = player.mission.try_pwd(pwd)
        if r:
            player.mission = None
            player.money += 1000
            player.location = "/"
            return "You have completed the mission. You have earned 1000⚛."
        elif r is False:
            player.mission = None
            return "You have failed the mission."
        else:
            return None
    if command == "ls":
        s = ""
        dict_location = player.mission.tree
        if player.location != "/":
            list_location = player.location.split("/")
            list_location.pop(0)
            for l in list_location:
                dict_location = dict_location[l]
        for n,t in dict_location.items():
            if type(t) == str:
                s+= f"-- {n}\n"
            else:
                s+= f"d- {n}\n"
        return s[:-1]
    if command.startswith("cat "):
        file = command[4:]
        dict_location = player.mission.tree
        if player.location != "/":
            list_location = player.location.split("/")
            list_location.pop(0)
            for l in list_location:
                dict_location = dict_location[l]
        if file in dict_location.keys():
            if type(dict_location[file]) == str:
                return dict_location[file]
            return "This is a folder, not a file."
        return "This file does not exist."
    if command.startswith("cd "):
        loc = command[3:]
        if loc == "..":
            if player.location == "/":
                return "You are already at the root of the mission."
            list_location = player.location.split("/")
            list_location.pop(-1)
            player.location = "/".join(list_location)
            return f"You are now in the {player.location} folder."
        dict_location = player.mission.tree
        if player.location != "/":
            list_location = player.location.split("/")
            list_location.pop(0)
            for l in list_location:
                dict_location = dict_location[l]
        if loc in dict_location.keys():
            if type(dict_location[loc]) == str:
                return "This is a file, not a folder."
            if player.location == "/":
                player.location += loc
            else:
                player.location += "/"+loc
            return f"You are now in the {player.location} folder."
        return "This folder does not exist."
    return "Command not found. Please try again with a valid command."