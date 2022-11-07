#!/usr/bin/env python3

"""
Starts the game

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import *
from display import reset_screen
from Statistics.rat_stats import PLAYER_RAT, BREEDS, BREED_NUMS, print_breeds

WELCOME = "Hello dearest Rat Adventurer. To begin your journey, please enter your name: "


def start():
    """
    Starts the game by getting the player's name and rat breed choice

    :return: None
    """
    reset_screen()

    # Prompts for name
    name = input(WELCOME)
    while not name:  # Catches empty names
        print("    ERROR: Name cannot be empty")
        name = input("Please enter your name: ")

    PLAYER_RAT["name"] = name
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

        while confirm not in "yn" and confirm != "yes" and confirm != "no":
            print(SELECTION_ERROR)
            print("You have chosen the breed: {}".format(breed.upper()))
            confirm = input("Is this your final choice [Y/N]? ").lower()
        confirm = True if confirm == 'y' or confirm == "yes" else False

        reset_screen()

    PLAYER_RAT["breed"] = breed
    PLAYER_RAT["stats"] = BREEDS[breed]

    print("Welcome to the Hazelwood Chateau, {} rat {}.\nWe hope you enjoy your stay.".format(breed, name))
    print(BANNER)
    print(RAT)
    input("Hit ENTER to start...")