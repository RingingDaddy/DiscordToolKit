import json
import sys

#initialize variables


this = sys.modules[__name__]

this.alttoken = None
this.maintoken = None

def loadsettings():
    with open("settings.json") as file:
        configfile = json.loads(file.read())
        file.close() # Release config file.

    this.maintoken = configfile['tokens']['main']
    this.alttoken  = configfile['tokens']['alt']
    print(maintoken)
    

def __main__():
    loadsettings()

if(__name__ == 'settingmanager'):
    __main__()
