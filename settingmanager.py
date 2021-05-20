import json
import sys

#initialize variables


this = sys.modules[__name__]

this.alttoken = None
this.maintoken = None
this.configfile = None

def loadsettings():
    with open("settings.json") as file:
        this.configfile = json.loads(file.read()) #Load config file into memory.
        file.close() # Release config file.

def get_setting(field, field2 = None):
    #TODO: make this not be extremely stupid
    if(field2 != None):
        print("configfile[{}][{}]".format(field, field2))
        return configfile[field][field2]
    else:
        return configfile[field]



def __main__():
    loadsettings()

if(__name__ == 'settingmanager'):
    __main__()
