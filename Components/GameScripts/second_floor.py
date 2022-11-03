#!/usr/bin/env python3

"""
Second floor specific encounters

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from copy import deepcopy
from assets import BANNER, MAP_ART
from ChateauMap.map import SECOND_FLOOR, LOCATIONS
from GameScripts.first_floor import discover_room

SECOND_LABEL = "HAZELWOOD CHATEAU - SECOND FLOOR - LOCATIONS DISCOVERED"
SECOND = {
# SECOND will be used as a global dictionary - this will be edited to determine what has been found
    "map": list("""     _______ _________________________________
    |       |          |                      |
    |       |           /                     |
    |       |          |                      |
    |       |____/_____|_____/_____           |
    |                              |          |
    |        ___________\___/______|__________|
    |       |             |                   |
    |       |             |                   |
    |       |             |                   |
    |_______|_____________|___________________|""")
}


def discover_second_stairs():
    """
    Since Stair Landing label is vertical, needs to be hardcoded

    :return: None
    """
    stairs = "Stair Landing"
    indices = [150, 198, 246, 294, 342, 390, 105, 153, 201, 249, 297, 345, 393]

    for i in range(len(indices)):
        SECOND["map"][indices[i]] = stairs[i]

    LOCATIONS[2][stairs]["found"] = True


def reset_second():
    """
    Resets the second floor

    :return: None
    """
    SECOND["map"] = deepcopy(MAP_ART["Second Empty"])

    for room in LOCATIONS[2]:
        LOCATIONS[2][room]["found"] = False


def print_second():
    """
    Prints the second floor map

    :return: None
    """
    print(BANNER, SECOND_LABEL, BANNER, ''.join(SECOND["map"]), BANNER, sep='\n')
    print("Unlocked Rooms:")
    for room in LOCATIONS[2]:
        if LOCATIONS[2][room]["found"]:
            print('    ', room)


def second_floor():
    pass


### USED TO TEST LOCATION LABEL PLACEMENTS ###
for room in LOCATIONS[2]:
    if room == "Stair Landing":
        discover_second_stairs()
    else:
        discover_room(room, SECOND, 2)

    print_second()
    reset_second()
