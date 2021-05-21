import json
import sys
from colorama import Fore, Back, Style

# initialize variables


this = sys.modules[__name__]

this.alttoken = None
this.maintoken = None
this.configfile = None
this.turningoff = False


def loadsettings():
    with open("settings.json") as file:
        # Load config file into memory.
        this.configfile = json.loads(file.read())

        file.close()  # Release config file.

def set_setting(field, field2=None, val=None):
    # TODO: make this not be extremely stupid aswell
    if(val==None):
        print(f"{Fore.Black}{Back.RED}The val field in set_setting() cannot be None!{Style.RESET_ALL}")

    if(field2 != None):
        configfile[field][field2] = val
    else:
        configfile[field] = val

def get_setting(field, field2=None):
    # TODO: make this not be extremely stupid
    if(field2 != None):
        return configfile[field][field2]
    else:
        return configfile[field]


def __main__():
    loadsettings()


if(__name__ == 'settingmanager'):
    __main__()
