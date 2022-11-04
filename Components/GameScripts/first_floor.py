#!/usr/bin/env python3

"""
First floor specific encounters

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from copy import deepcopy
from assets import BANNER
from display import reset_screen
from ChateauMap.map import FIRST_FLOOR
from ChateauMap.locations import LOCATIONS
from Statistics.rat_stats import PLAYER_RAT

FIRST_LABEL = "HAZELWOOD CHATEAU - FIRST FLOOR - LOCATIONS DISCOVERED"
FIRST = {
# FIRST will be used as a global dictionary - this will be edited to determine what has been found
    "map": list("""                            _______
                           |       |
                           |       |
     ___x__________________|__/ \__|__________
    |       |          |           |          |
    |       |          |          \           |
    |       |____/_____|___________|___/ \____|
    |       |                      |          |
    |        /                      /         |
    |       |__________/ \_________|          |
    |       |                      |          |
    |        /                      /         |
    |       |                      |          |
    |_______|______________________|__________|""")
}


def discover_room(room, map, floor):
    """
    Adds one of the horizontal room lables to the map

    :param room: str - Name of room
    :param map: list - Map of the floor
    :param floor: int - Floor that is being edited
    :return: None
    """
    words = room.split()  # Turns into a list

    for index in range(len(words)):
        word = words[index]
        start_index = LOCATIONS[floor][room]["start"][index]
        for i in range(start_index, start_index + len(word)):
            map["map"][i] = word[i - start_index]

    LOCATIONS[floor][room]["found"] = True


def discover_entryway():
    """
    Since Entryway label is vertical, needs to be hardcoded

    :return: None
    """
    entryway = "Entryway"
    indices = [213, 261, 309, 357, 405, 453, 501, 549]

    for i in range(len(indices)):
        FIRST["map"][indices[i]] = entryway[i]

    LOCATIONS[1][entryway]["found"] = True


def print_first():
    """
    Prints the first floor map

    :return: None
    """
    print(BANNER, FIRST_LABEL, BANNER, ''.join(FIRST["map"]), BANNER, sep='\n')


def first_floor():
    """
    Code to run the first floor

    :return: int floor - next floor number
    """
    room = "Entryway"

    while room != "Second Floor":
        reset_screen()
        if room == "Entryway":
            if LOCATIONS[1][room]["found"]:  # If entryway was already found
                pass
            else:
                print("    It's a dark and spooky night as Rat {} wakes up from a deep".format(PLAYER_RAT["name"]),
                "slumber within the walls of the Robinhold Chateau. The thunder booms shake the",
                "walls as {} realizes they are not where they are supposed to be. It's".format(PLAYER_RAT["name"]),
                "Ratsgiving for ratness sakes! They should be in the attic with the rest",
                "of their rat family eating rat food.")
                print("    Scrambling onto their paws, the rat looked around trying to remember",
                "where they were and how to get back to the attic. Unfortunately, {}".format(PLAYER_RAT["name"]),
                "has never been great at navigating ")
                

    return 2  # Rat goes up to floor two


### USED TO TEST LOCATION LABEL PLACEMENTS ###
# reset_map()
# for room in LOCATIONS[1]:
#     if room == "Entryway":
#         discover_entryway()
#     else:
#         discover_room(room, FIRST, 1)

#     print_first()
#     reset_first()
