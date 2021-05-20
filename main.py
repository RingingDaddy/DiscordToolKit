#!/usr/bin/env python3

import json
import discord
import settingmanager
import selfbot

class colors:
    """USAGE: print(colors.COLOR + TEXT + color.NONE) """
    CYAN   = '\033[96m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    NONE   = '\033[0m'

if __name__ == "__main__":

    print("Initializing Discord Toolkit")

    print('Main token: ' + settingmanager.get_setting("tokens", "main"))
    print('Alt token: '  + settingmanager.get_setting("tokens", "alt"))

    selfbot.start() #NO CODE WILL BE EXECUTED PAST THIS POINT

    