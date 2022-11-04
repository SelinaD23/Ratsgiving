#!/usr/bin/env python3

"""
Provides enemy stats for a run

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from random import randint
from ChateauMap.locations import LOCATIONS

ENEMIES = {
    "Mochi": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": []
    },
    "Matcha": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": []
    },
    "Maid Alexander": {
        "Speed": randint(8, 10),
        "Vision": randint(6, 8), 
        "Location": []
    },
    "Maid Selina": {
        "Speed": randint(6, 8),
        "Vision": randint(1, 6), 
        "Location": []
    },
    "Maid Sebastian": {
        "Speed": randint(6, 8),
        "Vision": randint(1, 6), 
        "Location": []
    },
    "Butler Apoorva": {
        "Speed": randint(6, 8),
        "Vision": randint(1, 6), 
        "Location": []
    },
    "Chef Kimberly": {
        "Speed": randint(6, 8),
        "Vision": randint(8, 10), 
        "Location": []
    },
    "Chef Jemma": {
        "Speed": randint(6, 8),
        "Vision": randint(6, 8), 
        "Location": []
    },
    "Mrs. Hazelwood": {
        "Speed": randint(6, 8),
        "Vision": randint(6, 8), 
        "Location": []
    },
    "Mr. Hazelwood": {
        "Speed": randint(8, 10),
        "Vision": randint(6, 8), 
        "Location": []
    },
    "Ms. Hazelwood": {
        "Speed": randint(2, 4),
        "Vision": randint(1, 6), 
        "Location": []
    }
}

BUTLER_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom", "Servant Room", "Laundry Room"],
    2: ["Stair Landing","Theater Room", "Game Room"],
    3: ["Stair Landing", "Office"]
}
CAT_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway"],
    2: ["Stair Landing", "Ms. Hazelwood's Bedroom", "Theater Room", "Game Room"],
    3: ["Stair Landing", "Master Bedroom", "Office", "Rat Hole"]
}
CHEF_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom", "Servant Room"]
}
FAMILY_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom"],
    2: ["Stair Landing", "Ms. Hazelwood's Bedroom", "Theater Room", "Game Room", "Bathroom"],
    3: ["Stair Landing", "Master Bedroom", "Ensuite Bathroom", "Office"]
}
MAID_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom", "Servant Room", "Laundry Room"],
    2: ["Stair Landing", "Ms. Hazelwood's Bedroom", "Theater Room", "Game Room", "Bathroom"],
    3: ["Stair Landing", "Master Bedroom", "Ensuite Bathroom", "Office", "Rat Hole"]
}


def assign_room(floor, room, person):
    """
    Moves the people from room to room 

    :return: None
    """ 
    if not ENEMIES[person]["Location"]:  # If the person was nowhere previously
        ENEMIES[person]["Location"] = [floor, room]
        LOCATIONS[floor][room]["occupants"].append(person)
    
    else:  # If person was in a room previously
        occupant_index = LOCATIONS[ENEMIES[person]["Location"][0]][ENEMIES[person]["Location"][1]]["occupants"].index(person)
        LOCATIONS[ENEMIES[person]["Location"][0]][ENEMIES[person]["Location"][1]]["occupants"].pop(occupant_index)
        ENEMIES[person]["Location"] = [floor, room]
        LOCATIONS[floor][room]["occupants"].append(person)


### USED FOR DEBUGGING ###
# def enemy_stats_debug():
#     """
#     Prints the ENEMIES dictionary (used for debugging)

#     :return: None
#     """

#     # Local variables to be used in loop
#     stats = ["Name", "Speed", "Vision", "Location"]

#     # Printing out the ENEMIES dictionary
#     for character in ENEMIES:
#         for stat in stats:
#             if stat == "Name":
#                 print("{}: {}".format(stat, character))
#             else:
#                 print("{}: {}".format(stat, ENEMIES[character][stat]))