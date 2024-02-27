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
    d.cprint('Welcome <New player> to the OctoConsole game.', d.Fore.GREEN)
    save['player']['name'] = d.cinput('What is your name? > ', d.Fore.WHITE, d.Fore.CYAN)
    player = Assets.player.Player(save['player']['name'])
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
    d.cprint(f'We are creating a new environment for you, {save["player"]["name"]}... Please wait...', d.Fore.GREEN)
else:
    d.cprint('Loading your environment... Please wait...', d.Fore.GREEN)
    player = Assets.player.Player(save['player']['name'], save['player']['inventory'], save['player']['computer'], save['player']['money'])

# Show the welcome message
time.sleep(3)
d.clear()
d.cprint(f'Welcome back,', d.Fore.GREEN)
d.cprint_art(save["player"]["name"], d.Fore.GREEN)

d.cprint("Welcome, remember that you can type \"help\" to get a list of commands and \"quit\" to quit the game.")
# The game loop:
playing = True
while playing:
    if player.mission is not None:
        choice = d.cinput(f"@{player.name}{player.location} {d.format_color_str('Mission:'+str(player.mission),d.Fore.YELLOW, d.Fore.GREEN)}> ", d.Fore.GREEN, d.Fore.CYAN)
        if "quit" in choice:
            d.cprint("You are going to quit during a mission, all progress will be lost and you will not be able to recover the money spent on the mission.", d.Fore.RED)
            if d.cinput("Are you sure? y/n > ", d.Fore.RED) in ["y","yes","Y","YES"]:
                playing = False
            else:
                d.cprint("Good choice.", d.Fore.GREEN)
        elif "help" in choice:
            d.cprint(Assets.commands.help_mission(), wait=0.001)
        else:
            r = Assets.commands.find_cmd_mission(choice, player)
            if r is not None:
                d.cprint(r)
    else:
        choice = d.cinput(f"@{player.name}{player.location} > ", d.Fore.GREEN, d.Fore.CYAN)
        if "quit" in choice:
            playing = False
        elif "help" in choice:
            d.cprint(Assets.commands.help(), wait=0.001)
        else:
            r = Assets.commands.find_cmd(choice, player)
            if r is not None:
                d.cprint(r)
    save['player']['name'] = player.name
    save['player']['inventory'] = player.inventory.items
    save['player']['money'] = player.money
    save['player']['computer'] = player.computer.inventory.items
    Assets.save.save(save)
d.cprint_art("Goodbye!", d.Fore.CYAN, "block2", 0.001)

##### ATTENTION! #####
### VERSION DE DEV ###

if d.cinput("Version de développement: vous alez supprimer le fichier de sauvegarde. y pour continuer. > ", d.Fore.RED, wait=0.001) == "y":
    save_file = 'save.json'
    if os.path.exists(save_file):
        os.remove(save_file)
        d.cprint('Save file deleted.', d.Fore.YELLOW)
    else:
        d.cprint('Save file does not exist.', d.Fore.RED)