#!/usr/bin/env python3

import json
import discord
import settingmanager
import selfbot
import menu
import threading
from colorama import Back, Fore, Style



class colors:
    """USAGE: print(colors.COLOR + TEXT + color.NONE) """
    CYAN = '\033[96m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    NONE = '\033[0m'

def toolkitexit():
    print(f"{Fore.BLACK}{Back.YELLOW}Exitting...{Style.RESET_ALL}")

    settingmanager.turningoff = True

    exit()


if __name__ == "__main__":

    print("Initializing Discord Toolkit")

    print('Main token: ' + settingmanager.get_setting("tokens", "main"))
    print('Alt token: ' + settingmanager.get_setting("tokens", "alt"))

    menuthread = threading.Thread(target=menu.begin)
    menuthread.start()

    try:
        selfbot.start()  # NO CODE WILL BE EXECUTED PAST THIS POINT
    except Exception as e:
        print(f"{Fore.BLACK}{Back.RED}{e}{Style.RESET_ALL}")

    toolkitexit() #This will only execute if the selfbot crashes for some reason, or if you turn off the app using CTRL + C
    
