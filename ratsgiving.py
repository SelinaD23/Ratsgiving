#!/usr/bin/env python3

"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""
from os import system, name
from assets import *
from rat_stats import BREEDS, BREED_NUMS, print_breeds
from end_screen import end_screen

WELCOME = "Hello dearest Rat Adventurer. To begin your journey, please enter your name: "
SELECTION_ERROR = "    ERROR: Selection invalid"


def reset_screen():
    """
    Clears the terminal and outputs the Ratsgiving title card

    :return: None
    """
    system('clear' if name == 'posix' else 'CLS')
    print(BANNER)
    print(TITLE)
    print(BANNER)


def start():
    """
    Starts the game by getting the player's name and rat breed choice

    :return: str name, str breed
    """
    reset_screen()

    # Prompts for name
    name = input(WELCOME)
    while not name:  # Catches empty names
        print("    ERROR: Name cannot be empty")
        name = input("Please enter your name: ")

    reset_screen()
    confirm = False

    # While the breed of rat has not been chosen
    while not confirm:
        print("Welcome, Adventurer {}. May the rats be with you and Smooth Tony guide your way...".format(name))
        print_breeds()

        breed = input("Please input your breed name or number: ").lower().title()

        # Tests to see if user entered a valid number value
        try:
            breed = BREED_NUMS[int(breed)]
        except ValueError:
            print(end="")
        except KeyError:
            print(end="")

        while breed not in BREEDS.keys():
            print(SELECTION_ERROR)
            breed = input("Please input your breed name: ").lower().title()
            try:
                breed = BREED_NUMS[int(breed)]
            except ValueError:
                print(end="")
            except KeyError:
                print(end="")

        print("You have chosen the breed: {}".format(breed.upper()))
        confirm = input("Is this your final choice [Y/N]? ").lower()

        while confirm not in "yn":
            print(SELECTION_ERROR)
            print("You have chosen the breed: {}".format(breed.upper()))
            confirm = input("Is this your final choice [Y/N]? ").lower()
        confirm = True if confirm == 'y' else False

        reset_screen()

    print("Welcome to the Hazelwood Chateau, {} rat {}.\nWe hope you enjoy your stay.".format(breed, name))
    print(BANNER)
    print(RAT)
    input("Hit ENTER to start...")
    system('clear' if name == 'posix' else 'CLS')

    return name, breed


def main():
    name, breed = start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        reset_screen()
        end_screen()
