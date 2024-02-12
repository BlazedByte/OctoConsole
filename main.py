from colorama import Fore
import time
import os

import Assets.display as d
import Assets.inventory
import Assets.player
import Assets.computer
import Assets.save
import Assets.commands

d.clear()

save = Assets.save.load()

# If the player is new, ask for their name
# If the player is not new, load their environment
if save['player']['name'] is None:
    d.cprint('Welcome <New player> to the OctoConsole game.', Fore.GREEN)
    save['player']['name'] = d.cinput('What is your name? > ', Fore.WHITE, Fore.CYAN)
    player = Assets.player.Player(save['player']['name'])
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
    d.cprint(f'We are creating a new environment for you, {save["player"]["name"]}... Please wait...', Fore.GREEN)
else:
    d.cprint('Loading your environment... Please wait...', Fore.GREEN)
    player = Assets.player.Player(save['player']['name'], save['player']['inventory'], save['player']['computer'], save['player']['money'])

# Show the welcome message
time.sleep(3)
d.clear()
d.cprint(f'Welcome back,', Fore.GREEN)
d.cprint_art(save["player"]["name"], Fore.GREEN)

d.cprint("Welcome, remember that you can type \"help\" to get a list of commands and \"quit\" to quit the game.")
# The game loop:
playing = True
while playing:
    choice = d.cinput(f"@{player.name}{player.location} > ", Fore.GREEN, Fore.CYAN)
    if "quit" in choice:
        playing = False
    elif "help" in choice:
        d.cprint(Assets.commands.help(), wait=0.01)
    else:
        r = Assets.commands.find(choice, player)
        if r is not None:
            d.cprint(r)
    save['player']['name'] = player.name
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
d.cprint_art("Goodbye!", Fore.CYAN, "block2", 0.001)

##### ATTENTION! #####
### VERSION DE DEV ###

if d.cinput("Version de développement: vous alez supprimer le fichier de sauvegarde. y pour continuer. > ", Fore.RED, wait=0.01) == "y":
    save_file = 'save.json'
    if os.path.exists(save_file):
        os.remove(save_file)
        d.cprint('Save file deleted.', Fore.YELLOW)
    else:
        d.cprint('Save file does not exist.', Fore.RED)