#!/usr/bin/env python3

"""
Provides enemy stats for a run

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from random import randint, choice

ENEMIES = {
    "Mochi": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": [],
        "Description": ""
    },
    "Matcha": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": [],
        "Description": ""
    },
    "Maid Alexander": {
        "Speed": randint(8, 10),
        "Vision": randint(6, 8), 
        "Location": []
    },
    "Maid Selina": {
        "Speed": randint(6, 8),
        "Vision": randint(4, 6), 
        "Location": []
    },
    "Maid Sebastian": {
        "Speed": randint(6, 8),
        "Vision": randint(4, 6), 
        "Location": []
    },
    "Butler Apoorva": {
        "Speed": randint(6, 8),
        "Vision": randint(4, 6), 
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
        "Vision": randint(4, 6), 
        "Location": []
    }
}
LOCATIONS = {
    1: {
        "Kitchen": "",
        "Living Room": "",
        "Dining Room": "",
        "Hallway": "",
        "Bathroom": "",
        "Servant Room": "",
        "Laundry Room": "",
        "Entryway": ""  # Stairs location
    },
    2: {
        "Stair Landing": "",
        "Bathroom": "",
        "Ms. Hazelwood's Bedroom": "",
        "Theater Room": "",
        "Game Room": "",
    },
    3: {
        "Stair Landing": "",
        "Master Bedroom": "",
        "Ensuite Bathroom": "",
        "Office": "",
        "Rat Hole": "",
    }
}
BUTLER_LOCATIONS = {
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom", "Servant Room"],
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
    1: ["Kitchen", "Living Room", "Dining Room", "Hallway", "Entryway", "Bathroom"],
    2: ["Stair Landing", "Ms. Hazelwood's Bedroom", "Theater Room", "Game Room", "Bathroom"],
    3: ["Stair Landing", "Master Bedroom", "Ensuite Bathroom", "Office", "Rat Hole"]
}


def starting_locations():
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
            room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room] and room in MAID_LOCATIONS[floor]])
            # Assign maid to room
            assign_room(floor, room, character)

            maid[floor - 1] = 1

        elif "Chef" in character:
            # Chefs only walk around the first floor
            # Finds all empty rooms on the floor and picks random room
            room = choice([room for room in LOCATIONS[1] if not LOCATIONS[1][room] and room in CHEF_LOCATIONS[1]])  
            # Assign chef to room
            assign_room(1, room, character)

        elif "Butler" in character:
            # Picks a random floor for butler start
            floor = randint(1, 3)
            # Finds all empty rooms on the floor and picks random room
            room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room] and room in BUTLER_LOCATIONS[floor]])
            # Assign butler to room
            assign_room(floor, room, character)

        elif "Hazelwood" in character:
            # Picks a random floor for family member start
            floor = randint(1, 3)
            # Finds all empty rooms on the floor and picks random room
            room = choice([room for room in LOCATIONS[floor] if not LOCATIONS[floor][room] and room in FAMILY_LOCATIONS[floor]])
            # Assign family member to room
            assign_room(floor, room, character)

        else:
            # Cats start on third floor
            # Finds all empty rooms on the floor and picks random room
            room = choice([room for room in LOCATIONS[3] if not LOCATIONS[3][room] and room in CAT_LOCATIONS[3]])  
            # Assign cat to room
            assign_room(1, room, character)



def assign_room(floor, room, person):
    """
    Moves the people from room to room 

    :return: None
    """ 
    if not ENEMIES[person]["Location"]:  # If the person was nowhere previously
        ENEMIES[person]["Location"] = [floor, room]
        LOCATIONS[floor][room] = person
    
    else:  # If person was in a room previously
        LOCATIONS[ENEMIES[person]["Location"][0]][ENEMIES[person]["Location"][1]] = ""
        ENEMIES[person]["Location"] = [floor, room]
        LOCATIONS[floor][room] = person


def enemy_stats_debug():
    """
    Prints the ENEMIES dictionary (used for debugging)

    :return: None
    """

    # Local variables to be used in loop
    stats = ["Name", "Speed", "Vision", "Location"]

    # Printing out the ENEMIES dictionary
    for character in ENEMIES:
        for stat in stats:
            if stat == "Name":
                print("{}: {}".format(stat, character))
            else:
                print("{}: {}".format(stat, ENEMIES[character][stat]))


def main():
    enemy_stats_debug()
    starting_locations()
    print("\n\n\n")
    enemy_stats_debug()
    starting_locations()
    print("\n\n\n")
    enemy_stats_debug()
    starting_locations()


main()