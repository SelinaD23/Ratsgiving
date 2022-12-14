#!/usr/bin/env python3

"""
General movements and escaping encounters

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import *
from random import random, randint


def room_actions(room):
    """
    Prints the choices for rat player

    :return: int choice
    """
    print(BANNER)
    print("Current Location: {} - How would you like to proceed?".format(room.upper()))
    print("    1: Look around the room for rat friends")
    print("    2: Look around the room for loot")
    print("    3: Peek into one of the next rooms")
    print("    4: Move into a different room")
    print("    5: View the map")
    print("    6: View your inventory")
    print(BANNER)

    move = input("Please enter your selection: ")

    while not (move.isdigit() and "1" <= move <= "6"):
        print(SELECTION_ERROR)
        move = input("Please enter your selection: ")
        
    print(BANNER)
    
    return int(move)


def find(total):
    """
    Looks for loot around the space

    :return: int num of loot found
    """
    return randint(0, total)


def inventory(inv):
    """
    Prints out the user inventory

    :param inv: dict Loot
    :return: None
    """
    print("YOUR INVENTORY:")
    empty = 0
    for loot in inv:
        if inv[loot] == 1:
            print("    1 {}".format(loot))

        elif inv[loot] > 0:
            if loot == "penny":
                term = "pennies"
            else:
                term = loot + "s"

            print("    {} {}".format(inv[loot], term))

        else:
            empty += 1

    if empty == len(inv):
        print("\x1B[3m" + "    empty" + "\x1B[0m")


def hide(rat_size, enemy_vision):
    """
    Determines if the rat player can escape from the enemy
    
    :return: bool hidden
    """
    if rat_size < enemy_vision:         # 75% chance of being hidden
        return random() < .75
    elif rat_size == enemy_vision:      # 50% chance of being hidden
        return random() < .5 
    elif rat_size - enemy_vision <= 2:  # 25% chance of being hidden
        return random() < .25
    else:                               # 5% chance of being hidden
        return random() < .5


def escape(rat_speed, enemy_speed):
    """
    Determines if the rat player can escape from the enemy
    
    :return: bool escape
    """
    if rat_speed > enemy_speed:         # 75% chance of escape
        return random() < .75
    elif rat_speed == enemy_speed:      # 50% chance of escape
        return random() < .5 
    elif enemy_speed - rat_speed <= 2:  # 25% chance of escape
        return random() < .25
    else:                               # 5% chance of escape
        return random() < .5


def fall(rat_balance):
    """
    Determines if the rat falls

    return bool fall
    """
    return random() > rat_balance / 14


def seek(rat_vision, rat_hearing):
    """
    Determines if the rat is able to see or hear into the next room

    return bool seek
    """
    return random() < rat_vision / 14 or random() < rat_hearing / 14
