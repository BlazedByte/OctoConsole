from colorama import Fore
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cprint(text, color):
    print(f"{color}{text}{Fore.RESET}")

def cinput(text, color):
    return input(f"{color}{text}{Fore.RESET}")