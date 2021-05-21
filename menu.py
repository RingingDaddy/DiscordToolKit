import sys
import time
import os
import settingmanager
from colorama import Fore, Back, Style

this = sys.modules[__name__]

this.logstate = False
this.inmenu = True


def renderPrompt():
    print(f"{Back.GREEN}{Fore.BLACK}Welcome to DiscordToolkit! To use the menu, type the appropriate button and press enter.{Style.RESET_ALL}")
    print(f"{Back.CYAN}{Fore.BLACK}1. Display Message Logger history")
    print(f"2. Temporarily enable bot message logging{Style.RESET_ALL}")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def logger():
    this.logstate = not this.logstate

    this.inmenu = True

    print(f"{Back.CYAN}{Fore.BLACK}Press ENTER to leave.{Style.RESET_ALL}")
    input()

    this.logstate = not this.logstate

    time.sleep(0.75) # Make sure the last message is sent

    clearConsole()  # After execution of command is done, clear the console.
    renderPrompt()


def togglefilterstate():
    currstate = settingmanager.get_setting("logger", "filterbotmessages")

    settingmanager.set_setting("logger", "filterbotmessages", not currstate)


# Update this to add more options.
options = {'1': logger, '2': togglefilterstate}


def begin():
    print("Initializing menu...")

    main()


"""Render main menu. Useful if you have nested menus, and don't """


def main():
    this.inmenu = True
    this.logstate = False

    renderPrompt()

    while True:
            try:
                option = input()

                if(settingmanager.turningoff == False):
                    options[option]()
                else:
                    break
            except Exception as e:
                print(
                    f"{Fore.BLACK}{Back.YELLOW}Failed to find option {e}{Style.RESET_ALL}")
        