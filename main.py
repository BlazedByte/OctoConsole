from colorama import Fore
import time
import os

from Assets.display import cprint, cprint_art, cinput, clear
import Assets.inventory
import Assets.player
import Assets.computer
import Assets.save
import Assets.commands

clear()

save = Assets.save.load()

# If the player is new, ask for their name
# If the player is not new, load their environment
if save['player']['name'] is None:
    cprint('Welcome <New player> to the OctoConsole game.', Fore.GREEN)
    save['player']['name'] = cinput('What is your name? > ', Fore.WHITE, Fore.BLUE)
    player = Assets.player.Player(save['player']['name'])
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
    cprint(f'We are creating a new environment for you, {save["player"]["name"]}... Please wait...', Fore.GREEN)
else:
    cprint('Loading your environment... Please wait...', Fore.GREEN)
    player = Assets.player.Player(save['player']['name'], save['player']['inventory'], save['player']['computer'], save['player']['money'])

# Show the welcome message
time.sleep(3)
clear()
cprint(f'Welcome back,', Fore.GREEN)
cprint_art(save["player"]["name"], Fore.GREEN)

cprint("Welcome, remember that you can type \"help\" to get a list of commands and \"quit\" to quit the game.")
# The game loop:
playing = True
while playing:
    choice = cinput(f"@{save['player']['name']}/ > ", Fore.GREEN, Fore.BLUE)
    if "quit" in choice:
        playing = False
    elif "help" in choice:
        cprint(Assets.commands.help(), wait=0.01)
    else:
        cprint(Assets.commands.find(choice))
cprint_art("Goodbye!", Fore.CYAN, "block2", 0.001)

##### ATTENTION! #####
### VERSION DE DEV ###

if cinput("Version de développement: vous alez supprimer le fichier de sauvegarde. y pour continuer. > ", Fore.RED) == "y":
    save_file = '/Users/nash115/Documents/GitHub/OctoConsole/save.json'
    if os.path.exists(save_file):
        os.remove(save_file)
        cprint('Save file deleted.', Fore.YELLOW)
    else:
        cprint('Save file does not exist.', Fore.RED)