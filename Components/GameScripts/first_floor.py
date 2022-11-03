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
from assets import BANNER, MAP_ART
from ChateauMap.map import FIRST_FLOOR, LOCATIONS, load_map

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


def reset_first():
    """
    Resets the first floor

    :return: None
    """
    FIRST["map"] = deepcopy(MAP_ART["First Empty"])

    for room in LOCATIONS[1]:
        LOCATIONS[1][room]["found"] = False


def print_first():
    """
    Prints the first floor map

    :return: None
    """
    print(BANNER, FIRST_LABEL, BANNER, ''.join(FIRST["map"]), BANNER, sep='\n')
    print("Unlocked Rooms:")
    for room in LOCATIONS[1]:
        if LOCATIONS[1][room]["found"]:
            print('    ', room)


def first_floor():
    pass


### USED TO TEST LOCATION LABEL PLACEMENTS ###

load_map()
for room in LOCATIONS[1]:
    if room == "Entryway":
        discover_entryway()
    else:
        discover_room(room, FIRST, 1)

    print_first()
    reset_first()
