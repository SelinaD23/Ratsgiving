#!/usr/bin/env python3

"""
Creates the floors using Nodes

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from random import choice, randint

LOCATIONS = {
    1: {
        "Kitchen": {
            "start": [242],
        },
        "Living Room": {
            "start": [512, 519]
        },
        "Dining Room": {
            "start": [435, 484]
        },
        "Hallway": {
            "start": [370]
        },
        "Bathroom": {
            "start": [219]
        },
        "Servant Room": {
            "start": [183, 232]
        },
        "Laundry Room": {
            "start": [64, 102]
        },
        "Entryway": {
        },  # Stairs location
    },
    2: {
        "Stair Landing": {
        },
        "Bathroom": {
            "start": [109]
        },
        "Ms. Hazelwood's Bedroom": {
            "start": [122, 126, 174]
        },
        "Theater Room": {
            "start": [416, 465]
        },
        "Game Room": {
            "start": [400, 448]
        }
    },
    3: {
        "Stair Landing": {
        },
        "Master Bedroom": {
            "start": [278, 315]
        },
        "Ensuite Bathroom": {
            "start": [99, 136]
        },
        "Office": {
            "start": [88]
            },
        "Rat Hole": {
        }
    }
}

class Room:
    def __init__(self, room):
        self.room = room
        self.connection1 = None
        self.connection2 = None
        self.connection3 = None
        self.connection4 = None

    def __repr__(self):
        return self.room

class Floor:
    def __init__(self, stair):
        self.stairs = stair


def load_map():
    """
    Loads the LOCATIONS dictionary with proper items

    :return: None
    """
    for floor in LOCATIONS:
        for room in LOCATIONS[floor]:
            LOCATIONS[floor][room]["occupants"] = []
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
    for floor in LOCATIONS:
        for room in LOCATIONS[floor]:
            if room == "Rat Hole":
                continue

            loot = ""
            for item in LOCATIONS[floor][room]["loot"]:
                

                if LOCATIONS[floor][room]["loot"][item] == 1:
                    loot += "1 {}, ".format(item)

                elif LOCATIONS[floor][room]["loot"][item] > 0:
                    if item == "penny":
                        term = "pennies"
                    else:
                        term = item + "s"

                    loot += "{} {}, ".format(LOCATIONS[floor][room]["loot"][item], term)

            loot = loot[:-2]  # Remove comma and space for formatting
            print("Floor {}, Room {}, has the following loot: {}".format(floor, room, loot))


def first_floor():
    """
    Creates the first floor map
                            _______
                           |Laundry|
                           | Room  |
     ___x__________________|__/ \__|__________
    |       |          |  Servant  |          |
    |   E   | Bathroom |   Room   \  Kitchen  |
    |   n   |____/_____|___________|___/ \____|
    |   t   |                      |   D      |
    |   r    /       Hallway        /  i  R   |
    |   y   |__________/ \_________|   n  o   |
    |   w   |                      |   i  o   |
    |   a    /     Living Room      /  n  m   |
    |   y   |                      |   g      |
    |_______|______________________|__________|
    
    :return: Floor first_floor
    """

    # Create the rooms
    entry = Room("Entryway")
    living = Room("Living Room")
    hall = Room("Hallway")
    bathroom = Room("Bathroom")
    kitchen = Room("Kitchen")
    laundry = Room("Laundry Room")
    dining = Room("Dining Room")
    servant = Room("Servant Room")

    # Link the rooms up
    entry.connection1, entry.connection2 = living, hall
    hall.connection1, hall.connection2, hall.connection3, hall.connection4 = entry, living, bathroom, dining
    bathroom.connection1 = hall
    living.connection1, living.connection2, living.connection3 = entry, hall, dining
    dining.connection1, dining.connection2, dining.connection3 = hall, living, kitchen
    kitchen.connection1, kitchen.connection2 = dining, servant
    servant.connection1, servant.connection2 = kitchen, laundry
    laundry.connection1 = servant

    return entry


def second_floor():
    """
    Creates the second floor map
     _______ _________________________________
    |       |          |                      |
    |     L | Bathroom  /  Ms. Hazelwood's    |
    |  S  a |          |        Room          |
    |  t  n |____/_____|_____/_____           |
    |  a  d                        |          |
    |  i  i  ___________\___/______|__________|
    |  r  n |             |                   |
    |     g |    Game     |      Theater      |
    |       |    Room     |       Room        |
    |_______|_____________|___________________|
    
    :return: Floor second_floor
    """

    # Create the rooms
    bathroom = Room("Bathroom")
    stair = Room("Stair Landing")
    bedroom = Room("Ms. Hazelwood's Bedroom")
    theater = Room("Theater Room")
    game = Room("Game Room")

    # Link the rooms up
    stair.connection1, stair.connection2, stair.connection3, stair.connection4 = bathroom, bedroom, theater, game
    bathroom.connection1, bathroom.connection2 = bedroom, stair
    bedroom.connection1, bedroom.connection2 = bathroom, stair
    theater.connection1 = stair
    game.connection1 = stair

    return stair


def third_floor():
    """
    Creates the third floor map

     ___o___ ______________________
    |       |          |           |
    |     L |  Office  |  Ensuite  |
    |  S  a  /         |  Bathroom |
    |  t  n |__________|_____/_____|
    |  a  d |                      |          
    |  i  i |                      |
    |  r  n |       Master         |
    |     g |       Bedroom        |
    |       |                      |
    |_______|______________________|
    
    :return: Floor third_floor
    """

    # Create the rooms
    bathroom = Room("Ensuite Bathroom")
    stair = Room("Stair Landing")
    bedroom = Room("Master Bedroom")
    hole = Room("Rat Hole")
    office = Room("Office")

    # Link the rooms up
    stair.connection1, stair.connection2, stair.connection3 = hole, bedroom, office
    bathroom.connection1 = bedroom
    bedroom.connection1, bedroom.connection2 = bathroom, stair
    hole.connection1 = stair
    office.connection1 = stair

    return stair


FIRST_FLOOR = Floor(first_floor())
SECOND_FLOOR = Floor(second_floor())
THIRD_FLOOR = Floor(third_floor())