"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""
from os import system, name
from rat_stats import BREEDS, BREED_NUMS, print_breeds

TITLE = """ ██████╗░░█████╗░████████╗░██████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░██████╗░
 ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝░██║██║░░░██║██║████╗░██║██╔════╝░
 ██████╔╝███████║░░░██║░░░╚█████╗░██║░░██╗░██║╚██╗░██╔╝██║██╔██╗██║██║░░██╗░
 ██╔══██╗██╔══██║░░░██║░░░░╚═══██╗██║░░╚██╗██║░╚████╔╝░██║██║╚████║██║░░╚██╗
 ██║░░██║██║░░██║░░░██║░░░██████╔╝╚██████╔╝██║░░╚██╔╝░░██║██║░╚███║╚██████╔╝
 ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░"""
BANNER = "============================================================================="
WELCOME = "Hello dearest Rat Adventurer. To begin your journey, please enter your name: "
SELECTION_ERROR = "\tERROR: Selection invalid"


def reset_screen():
    system('clear' if name == 'posix' else 'CLS')
    print(BANNER)
    print(TITLE)
    print(BANNER)


def start():
    reset_screen()

    name = input(WELCOME)
    while not name:
        print("\tERROR: Name cannot be empty")
        name = input("Please enter your name: ")

    reset_screen()
    confirm = False

    while not confirm:
        print("Welcome, Adventurer {}. May the rats be with you and Smooth Tony guide your way...".format(name))
        print_breeds()

        breed = input("Please input your breed name or number: ").lower().title()

        try:
            breed = BREED_NUMS[int(breed)]
        except ValueError:
            pass

        while breed not in BREEDS.keys():
            print(SELECTION_ERROR)
            print_breeds()
            breed = input("Please input your breed name: ").lower().title()
            try:
                breed = BREED_NUMS[int(breed)]
            except ValueError:
                pass

        print("You have chosen the breed: {}".format(breed.upper()))
        confirm = input("Is this your final choice [Y/N]? ").lower()

        while confirm not in "yn":
            print(SELECTION_ERROR)
            print("You have chosen the breed: {}".format(breed.upper()))
            confirm = input("Is this your final choice [Y/N]? ").lower()
        confirm = True if confirm == 'y' else False

        reset_screen()

    print("Welcome to the Hazelwood Chateau, {} rat {}.\nWe hope you enjoy your stay.\n\n".format(breed, name))
    input("Hit ENTER to start...")
    system('clear' if name == 'posix' else 'CLS')

    return name, breed


def main():
    name, breed = start()


main()
