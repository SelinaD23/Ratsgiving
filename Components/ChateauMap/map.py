#!/usr/bin/env python3

"""
Creates the floors using Nodes

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

LOCATIONS = {
    1: {
        "Kitchen": [],
        "Living Room": [],
        "Dining Room": [],
        "Hallway": [],
        "Bathroom": [],
        "Servant Room": [],
        "Laundry Room": [],
        "Entryway": []  # Stairs location
    },
    2: {
        "Stair Landing": [],
        "Bathroom": [],
        "Ms. Hazelwood's Bedroom": [],
        "Theater Room": [],
        "Game Room": []
    },
    3: {
        "Stair Landing": [],
        "Master Bedroom": [],
        "Ensuite Bathroom": [],
        "Office": [],
        "Rat Hole": []
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
    def __init__(self):
        self.stairs = None


def first_floor():
    """
    Creates the first floor map
                          Laundry Room
                               |
                          Servant Room
                               |
             Bathroom      Kitchen
                 |             |
    Entryway - Hallway  -  Dining Room
       |         |             |
       ---  Living Room  -------
    
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


def second_floor():
    """
    Creates the second floor map
               Theater Room 
                    |            
    Bathroom - Stair Landing  -  Game Room
       |            |            
       ---  Ms. Hazelwood's Bedroom 
    
    :return: Floor first_floor
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


def third_floor():
    """
    Creates the third floor map
      Rat Hole
         |                   
    Stair Landing - Master Bedroom
         |                |            
       Office      Ensuite Bathroom
    
    :return: Floor first_floor
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


FIRST_FLOOR = first_floor()
SECOND_FLOOR = second_floor()