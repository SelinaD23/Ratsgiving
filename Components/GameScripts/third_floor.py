#!/usr/bin/env python3

"""
Second floor specific encounters

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import BANNER, MAP_ART
from ChateauMap.map import THIRD_FLOOR
from ChateauMap.locations import LOCATIONS

THIRD_LABEL = "HAZELWOOD CHATEAU - THIRD FLOOR MAP"
THIRD = {
# THIRD will be used as a global dictionary - this will be edited to determine what has been found
    "map": list("""     _______ ______________________
    |       |          |           |
    |       |          |           |
    |        /         |           |
    |       |__________|_____/_____|
    |       |                      |
    |       |                      |
    |        /                      |
    |       |                      |
    |       |                      |
    |_______|______________________|""")
}


def discover_third_stairs():
    """
    Since Stair Landing label is vertical, needs to be hardcoded

    :return: None
    """
    stairs = "Stair Landing"
    indices = [117, 154, 191, 228, 265, 302, 83, 120, 157, 194, 231, 268, 305]

    for i in range(len(indices)):
        THIRD["map"][indices[i]] = stairs[i]

    LOCATIONS[3][stairs]["found"] = True


def discover_rat_hole():
    """
    Changes rat hole label upon discovery

    :return: None
    """
    THIRD["map"][33] = "o"

    LOCATIONS[3]["Rat Hole"]["found"] = True


def print_third():
    """
    Prints the third floor map

    :return: None
    """
    print(BANNER, THIRD_LABEL, BANNER, ''.join(THIRD["map"]), BANNER, sep='\n')
    print("Unlocked Rooms:")
    for room in LOCATIONS[3]:
        if LOCATIONS[3][room]["found"]:
            print('    ', room)


def third_floor():
    """
    Code to run the third floor

    :return: int floor - next floor number or string "Attic"
    """
    pass


### USED TO TEST LOCATION LABEL PLACEMENTS ###
# for room in LOCATIONS[3]:
#     if room == "Stair Landing":
#         discover_third_stairs()
#     elif room == "Rat Hole":
#         discover_rat_hole()
#     else:
#         discover_room(room, THIRD, 3)

#     print_third()
#     reset_third()
