from colorama import Fore
import time
import os

from Assets.display import cprint, cinput, clear
import Assets.inventory
import Assets.player
import Assets.computer
import Assets.save

clear()

save = Assets.save.load()

if save['player']['name'] is None:
    cprint('Welcome <New player> to the OctoConsole game.', Fore.GREEN)
    save['player']['name'] = cinput('What is your name? > ', Fore.WHITE)
    player = Assets.player.Player(save['player']['name'])
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
    cprint(f'We are creating a new environment for you, {save["player"]["name"]}... Please wait...', Fore.GREEN)
else:
    cprint('Loading your environment... Please wait...', Fore.GREEN)
    player = Assets.player.Player(save['player']['name'], save['player']['inventory'], save['player']['computer'], save['player']['money'])

time.sleep(3)
clear()
cprint(f'Welcome back, {save["player"]["name"]}!', Fore.GREEN)

##### ATTENTION! #####
### VERSION DE DEV ###

if cinput("Version de développement: vous alez supprimer le fichier de sauvegarde. y pour continuer. > ", Fore.RED) == "y":
    save_file = '/Users/nash115/Documents/GitHub/OctoConsole/save.json'
    if os.path.exists(save_file):
        os.remove(save_file)
        cprint('Save file deleted.', Fore.YELLOW)
    else:
        cprint('Save file does not exist.', Fore.RED)