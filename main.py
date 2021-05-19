#!/usr/bin/env python3

import json
import discord
import settingmanager

class colors:
    """USAGE: print(colors.COLOR + TEXT + color.NONE) """
    CYAN   = '\033[96m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    NONE   = '\033[0m'

print(colors.CYAN + 'Initializing DiscordToolkit...')

print('Main token: ' + settingmanager.maintoken)
print('Alt token: '  + settingmanager.alttoken + colors.NONE)

    