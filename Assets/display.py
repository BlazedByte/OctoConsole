from colorama import Fore
import os
import time
import art

def clear():
    print(Fore.RESET)
    os.system('cls' if os.name == 'nt' else 'clear')

def format_color_str(thing:str, color=Fore.RESET, reset_color=Fore.RESET) -> str:
    return f"{color}{thing}{reset_color}"

def cprint(thing:str, color=Fore.RESET, wait:float=0.03) -> None:
    """Prints a string progressively, as if it were being typed out.

    Parameters
    ----------
    thing : str
        The string to be printed progressively.
    wait : float, optional
        The time in s between each caracter, by default 0.1
    """
    thing = str(thing)
    print(color, end='', flush=True)
    for i in thing:
        print(f"{i}", end='', flush=True)
        time.sleep(wait)
    print(Fore.RESET)

def cinput(thing:str, color=Fore.RESET, input_color=Fore.RESET, wait:float=0.03) -> str:
    """Prints a string progressively, as if it were being typed out.

    Parameters
    ----------
    thing : str
        The string to be printed progressively.
    wait : float, optional
        The time in s between each caracter, by default 0.1
    """
    thing = str(thing)
    print(color, end='', flush=True)
    for i in thing:
        print(f"{i}", end='', flush=True)
        time.sleep(wait)
    print(input_color, end='', flush=True)
    response = input("")
    print(Fore.RESET, end='', flush=True)
    return response

def cprint_art(thing:str, color=Fore.RESET, font="sub-zero", wait:float=0.003) -> None:
    thing = str(thing)
    thing = art.text2art(thing, font=font)
    cprint(thing, color, wait)