import sys
import time
from colorama import Fore, Back, Style


def begin():
    print("Initializing menu...")

    main()


def main():
    print(f"{Back.GREEN}{Fore.BLACK}Welcome to DiscordToolkit! To use the menu, type the appropriate button and press enter.{Style.RESET_ALL}")

    while True:
        # For now this does nothing, this is a loop for the menu to run it's code.
        pass
