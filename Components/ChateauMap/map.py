#!/usr/bin/env python3

"""
Creates the floors using Nodes

Programmed by: Selina Ding
https://github.com/SelinaD23
"""


class Room:
    def __init__(self, room):
        self.room = room
        self.connection1 = None
        self.connection2 = None
        self.connection3 = None
        self.connection4 = None

    def __repr__(self):
        return self.room

    def next_room(self):
        next = []
        if self.connection1 is not None:
            next.append(self.connection1.room)
        if self.connection2 is not None:
            next.append(self.connection2.room)
        if self.connection3 is not None:
            next.append(self.connection3.room)
        if self.connection4 is not None:
            next.append(self.connection4.room)
        return next


class Floor:
    def __init__(self, room):
        self.room = room

    def next_room(self):
        return self.room.next_room()

    def move(self, room):
        if self.room.connection1.room == room:
            return self.room.connection1
        elif self.room.connection2.room == room:
            return self.room.connection2
        elif self.room.connection3.room == room:
            return self.room.connection3
        else:
            return self.room.connection4


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

     _______ ____________________o_
    |       |          |           |
    |     L |  Office  |  Ensuite  |
    |  S  a  /         |  Bathroom |
    |  t  n |__________|_____/_____|
    |  a  d |                      |          
    |  i  i |                      |
    |  r  n  /      Master         |
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
    stair.connection1, stair.connection2 = bedroom, office
    bathroom.connection1, bathroom.connection2 = bedroom, hole
    bedroom.connection1, bedroom.connection2 = bathroom, stair
    hole.connection1 = bathroom
    office.connection1 = stair

    return stair


FIRST_FLOOR = Floor(first_floor())
SECOND_FLOOR = Floor(second_floor())
THIRD_FLOOR = Floor(third_floor())