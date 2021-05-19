import json

#initialize variables

alttoken = ""
maintoken = ""

def loadsettings():
    with open("settings.json") as file:
        configfile = json.loads(file.read())
        file.close() # Release config file.

    maintoken = configfile['tokens']['main']
    alttoken  = configfile['tokens']['alt']
    

def __main__():
    loadsettings()
    print("LOADED SUCCESFULLY")

if(__name__ == "__main__"):
    __main__()
