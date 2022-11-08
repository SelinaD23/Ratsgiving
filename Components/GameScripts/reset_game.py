#!/usr/bin/env python3

"""
Resets the game

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Statistics.enemies import *
from assets import * 
from copy import deepcopy
from random import randint, choice
from ChateauMap.locations import LOCATIONS
from GameScripts.chateau import FIRST, SECOND, THIRD
from Statistics.rat_stats import RAT_FRIENDS


def reset_map():
    """
    Resets the game

    :return: None
    """
    for floor in LOCATIONS:
        for room in LOCATIONS[floor]:
            LOCATIONS[floor][room]["occupants"] = []
            LOCATIONS[floor][room]["rats"] = []
            LOCATIONS[floor][room]["found"] = False
            LOCATIONS[floor][room]["loot"] = {
                "stick": 0,
                "seed": 0,
                "cheese": 0,
                "penny": 0,
                "nickel": 0,
                "dime": 0,
                "quarter": 0
            }

    remove_enemies_and_friends()  # Clears the map of enemies
    reset_first()   # Resets first floor
    reset_second()  # Resets second floor
    reset_third()   # Resets third floor
    load_enemies()  # Places enemies
    load_rats()     # Places rat friends
    generate_loot() # Generates loot

def reset_first():
    """
    Resets the first floor

    :return: None
    """
    FIRST["map"] = deepcopy(MAP_ART["First Empty"])

    for room in LOCATIONS[1]:
        LOCATIONS[1][room]["found"] = False


def reset_second():
    """
    Resets the second floor

    :return: None
    """
    SECOND["map"] = deepcopy(MAP_ART["Second Empty"])

    for room in LOCATIONS[2]:
        LOCATIONS[2][room]["found"] = False


def reset_third():
    """
    Resets the third floor

    :return: None
    """
    THIRD["map"] = deepcopy(MAP_ART["Third Empty"])

    for room in LOCATIONS[3]:
        LOCATIONS[3][room]["found"] = False


def remove_enemies_and_friends():
    """
    Removes all the enemies and other rats from the map

    :return: None
    """

    for character in ENEMIES:
        ENEMIES[character]["Location"] = ""

    for floor in LOCATIONS:
        for room in LOCATIONS[floor]:
            LOCATIONS[floor][room]["occupants"] = []


def load_enemies():
    """
    Puts all the enemies into the game

    :return: None
    """ 
    maid = [0, 0, 0]
    for character in ENEMIES:
        if "Maid" in character:
            # One maid on each floor to start
            floor = randint(1, 3)
            while maid[floor - 1]:
                floor = randint(1, 3)

            # Finds all empty rooms Maids can enter on the floor and picks random room
            room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room]["occupants"] and room in MAID_LOCATIONS[floor]])
            # Assign maid to room
            assign_room(floor, room, character)

            maid[floor - 1] = 1

        elif "Chef" in character:
            # Chefs only walk around the first floor
            # Finds all empty rooms on the floor and picks random room
            room = choice([room for room in LOCATIONS[1] if not LOCATIONS[1][room]["occupants"] and room in CHEF_LOCATIONS[1]])  
            # Assign chef to room
            assign_room(1, room, character)

        elif "Butler" in character:
            # Picks a random floor for butler start
            floor = randint(2, 3)
            # Finds all empty rooms on the floor and picks random room
            room = ""
            while not room:
                try:
                    room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room]["occupants"] and room in BUTLER_LOCATIONS[floor]])
                except IndexError:
                    # Picks the other floor for butler start
                    floor = randint(1, 3)
            # Assign butler to room
            assign_room(floor, room, character)

        elif "Hazelwood" in character:
            # Picks a random floor for family member start
            floor = randint(1, 3)
            # Finds all empty rooms on the floor and picks random room
            room = ""
            while not room:
                try:
                    room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room]["occupants"] and room in FAMILY_LOCATIONS[floor]])
                except IndexError:
                    # Picks a new random floor for family member start
                    floor = randint(1, 3)

            # Assign family member to room
            assign_room(floor, room, character)

        else:
            # Cats start on third floor unless third floor is full
            # Finds all empty rooms on the floor and picks random room
            floor = 3
            room = ""
            while not room:
                try:
                    room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room]["occupants"] and room in CAT_LOCATIONS[floor]])
                except IndexError:
                    floor = 2
            # Assign cat to room
            assign_room(floor, room, character)


def load_rats():
    """
    Puts all the rats into the game

    :return: None
    """ 
    for rat in RAT_FRIENDS:
        floor = randint(1, 3)
        room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room]["rats"]])
        LOCATIONS[floor][room]["rats"].append(rat)


def generate_loot():
    """
    Generates and fills the Chateau with loot

    :return: None
    """
    loot = {
        "stick": randint(1,10),
        "seed": randint(1,20),
        "cheese": randint(1,5),
        "penny": randint(1,20),
        "nickel": randint(1,10),
        "dime": randint(1,10),
        "quarter": randint(1,5)
    }

    total_loot = []

    for item in loot:
        for _ in range(loot[item]):
            total_loot.append(item)

    total = len(total_loot)

    # Puts the loot into random rooms
    for _ in range(total):
        floor = randint(1, 3)
        room = choice(list(LOCATIONS[floor]))
        while room == "Rat Hole":
            room = choice(list(LOCATIONS[floor]))

        loot_choice = total_loot.pop(total_loot.index(choice(total_loot)))
        LOCATIONS[floor][room]["loot"][loot_choice] += 1
        
    ### Debugging ###
    # for floor in LOCATIONS:
    #     for room in LOCATIONS[floor]:
    #         if room == "Rat Hole":
    #             continue

    #         loot = ""
    #         for item in LOCATIONS[floor][room]["loot"]:
                

    #             if LOCATIONS[floor][room]["loot"][item] == 1:
    #                 loot += "1 {}, ".format(item)

    #             elif LOCATIONS[floor][room]["loot"][item] > 0:
    #                 if item == "penny":
    #                     term = "pennies"
    #                 else:
    #                     term = item + "s"

    #                 loot += "{} {}, ".format(LOCATIONS[floor][room]["loot"][item], term)

    #         loot = loot[:-2]  # Remove comma and space for formatting
    #         print("Floor {}, Room {}, has the following loot: {}".format(floor, room, loot))