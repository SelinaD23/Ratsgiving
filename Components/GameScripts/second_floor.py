#!/usr/bin/env python3

"""
Second floor specific encounters

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import BANNER
from ChateauMap.map import SECOND_FLOOR
from ChateauMap.locations import LOCATIONS

SECOND_LABEL = "HAZELWOOD CHATEAU - SECOND FLOOR MAP"
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
    """
    Code to run the first floor

    :return: int floor - next floor number
    """
    pass


### USED TO TEST LOCATION LABEL PLACEMENTS ###
# for room in LOCATIONS[2]:
#     if room == "Stair Landing":
#         discover_second_stairs()
#     else:
#         discover_room(room, SECOND, 2)

#     print_second()
#     reset_second()
