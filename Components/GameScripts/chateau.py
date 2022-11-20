#!/usr/bin/env python3

"""
Runs the entire game

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import BANNER
from random import choice
from display import reset_screen
from ChateauMap.locations import LOCATIONS
from Components.end_screen import loss_ending
from Statistics.rat_stats import PLAYER_RAT, RAT_FRIENDS
from Statistics.enemies import *
from GameScripts.movement import *

FIRST_LABEL = " HAZELWOOD CHATEAU - FIRST FLOOR - LOCATIONS DISCOVERED"
SECOND_LABEL = " HAZELWOOD CHATEAU - SECOND FLOOR - LOCATIONS DISCOVERED"
THIRD_LABEL = " HAZELWOOD CHATEAU - THIRD FLOOR - LOCATIONS DISCOVERED"
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

CONNECTIONS= {
    (1, "Entryway"): ["Second Floor", "Hallway", "Living Room"],
    (1, "Bathroom"): ["Hallway"],
    (1, "Hallway"): ["Entryway", "Bathroom", "Living Room", "Dining Room"],
    (1, "Living Room"): ["Entryway", "Hallway", "Dining Room"],
    (1, "Dining Room"): ["Hallway", "Living Room", "Kitchen"],
    (1, "Kitchen"): ["Dining Room", "Servant Room"],
    (1, "Servant Room"): ["Kitchen", "Laundry Room"],
    (1, "Laundry Room"): ["Servant Room"],
    (2, "Stair Landing"): ["Ground Floor", "Bathroom", "Ms. Hazelwood's Bedroom", "Game Room", "Theater Room", "Third Floor"],
    (2, "Game Room"): ["Stair Landing"],
    (2, "Theater Room"): ["Stair Landing"],
    (2, "Ms. Hazelwood's Bedroom"): ["Stair Landing", "Bathroom"],
    (2, "Bathroom"): ["Stair Landing", "Ms. Hazelwood's Bedroom"],
    (3, "Stair Landing"): ["Second Floor", "Office", "Master Bedroom"],
    (3, "Office"): ["Stair Landing"],
    (3, "Master Bedroom"): ["Stair Landing", "Ensuite Bathroom"],
    (3, "Ensuite Bathroom"): ["Master Bedroom", "Rat Hole"],
    (3, "Rat Hole"): ["Ensuite Bathroom"]
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


def print_map(floor):
    """
    Prints the map

    :return: None
    """
    if floor == 1:
        print(FIRST_LABEL, BANNER, ''.join(FIRST["map"]), sep='\n')
    elif floor == 2:
        print(SECOND_LABEL, BANNER, ''.join(SECOND["map"]), sep='\n')
    else:
        print(THIRD_LABEL, BANNER, ''.join(THIRD["map"]), sep='\n')


### USED TO TEST LOCATION LABEL PLACEMENTS ###
# reset_map()
# for room in LOCATIONS[1]:
#     if room == "Entryway":
#         discover_entryway()
#     else:
#         discover_room(room, FIRST, 1)

#     print_first()
#     reset_first()


def detect(floor, room):
    """
    Determines if enemies detect rat

    :param floor: int - current floor
    :param room: str - current room
    :return: None if not caught, Bool play again if caught
    """
    for person in LOCATIONS[floor][room]["occupants"]:
        # If the rat could not hide
        if not hide(PLAYER_RAT["stats"]["Size"], ENEMIES[person]["Vision"]):
            input("    Oh no! {} has been spotted by {}! Hit ENTER to run...".format(PLAYER_RAT["name"], person))
            # If escapes
            if escape(PLAYER_RAT["stats"]["Speed"], ENEMIES[person]["Speed"]):
                print("        Made it away safely!")
            else:
                return loss_ending(room, person, floor)
        else:
            print("    {} did not see {}!".format(person, PLAYER_RAT["name"]))


def print_enemies(floor, room):
    """
    Prints the enemies in the room

    :param floor: int - current floor
    :param room: str - current room
    :return: bool - if enemies are in the room
    """
    # If the occupants list is empty
    if not LOCATIONS[floor][room]["occupants"]:
        print("    There is no one currently in the {}".format(room))
        return False

    # Printing enemies in room
    if len(LOCATIONS[floor][room]["occupants"]) > 1:
        if len(LOCATIONS[floor][room]["occupants"]) > 2: 
            for i in range(len(LOCATIONS[floor][room]["occupants"]) - 1):
                print(LOCATIONS[floor][room]["occupants"][i] + ",", sep=" ")
        else:
            print(LOCATIONS[floor][room]["occupants"][0], sep=" ")
        print("and {} are in the {}".format(LOCATIONS[floor][room]["occupants"][-1], room))
    else:
        print("{} is in the {}".format(LOCATIONS[floor][room]["occupants"][0], room))
    
    return True

                    
def first_floor():
    """
    Code to run the first floor

    :return: int floor - next floor number
    """
    room = "Entryway"

    while room != "Second Floor":
        reset_screen()
        next = CONNECTIONS[(1, room)]
        occupied = True

        if room == "Entryway":
            if LOCATIONS[1][room]["found"]:  # If entryway was already found
                # See if enemies sees Rat entering
                if LOCATIONS[1][room]["occupants"]:
                    print("Entering the Entryway...")
                    enter = detect(1, room)
                    if isinstance(enter, bool):
                        return enter
                    print(BANNER)
                print("    Walking back into the Entryway, the storm outside is still going.")
                print("Best hurry up and get up to the attic before Ratsgiving is over.")
            else:
                ### START OF GAME EXPOSITION AND GOALS ###
                print("    It's a dark and spooky night as Rat {} wakes up from a deep slumber".format(PLAYER_RAT["name"]))
                print("within the walls of the Hazelwood Chateau. The thunder booms shake the")
                print("beams as {} realizes they are not where they are supposed to be. It's".format(PLAYER_RAT["name"]))
                print("Ratsgiving for ratness sakes! They should be in the attic with the rest")
                print("of their rat family eating rat food.")
                print("    Scrambling onto their paws, the rat looked around trying to remember")
                print("where they were and how to get back to the attic. Unfortunately, {}".format(PLAYER_RAT["name"]))
                print("has never been great at navigating the large chateau and is drawing a blank.")
                print("All they remember is the only way to make it to the attic is through the rat")
                print("hole located somewhere on the third floor.")
                print("    {} realizes they should also stop to look for things for the".format(PLAYER_RAT["name"]))
                print("Ratsgiving table since they will be showing up for dinner too late. Maybe")
                print("the chateau will have hidden food and offerings for {} to find? In".format(PLAYER_RAT["name"]))
                print("any case, {} will need to avoid the people and cats living in the".format(PLAYER_RAT["name"]))
                print("chateau if they want to make it to dinner safe. Perhaps some friends might")
                print("also be around to bring to the family?")
                print(BANNER)
                print("\x1B[3m" + "YOUR MISSION:" + "\x1B[0m")
                print("\x1B[3m" + "    - Gather at least 5 loot items to be allowed to join the Ratsgiving dinner" + "\x1B[0m")
                print("\x1B[3m" + "    - Find and bring at least 1 rat friend to the Ratsgiving celebration" + "\x1B[0m")
                print("\x1B[3m" + "    - Get back to the attic without dying and without your rat friend dying" + "\x1B[0m")
                print(BANNER)
                input("Hit ENTER to proceed into the Chateau's Entryway...")
                reset_screen()

                ### ENTRYWAY DESCRIPTION AND ACTIONS ###
                discover_entryway()

                print("    Peering out from the hole in the wall into the Entryway of the")
                print("Chateau, the chandler hanging from the ceiling glimmers bright overhead.")
                print("Cautiously stepping forward, {} looks around.".format(PLAYER_RAT["name"]))

        # Rest of Chateau
        else:
            # See if the enemies see the rat
            if LOCATIONS[1][room]["occupants"]:
                print("Entering the {}...".format(room))
                enter = detect(1, room)
                if isinstance(enter, bool):
                    return enter
                print(BANNER)
            
            # Discover the room
            if not LOCATIONS[1][room]["found"]:
                discover_room(room, FIRST, 1)

        # Prints if enemies are in the room
        occupied = print_enemies(1, room)

        # Runs options until Rat moves
        room = run_actions(1, room, occupied, next)

        # If rat gets caught trying to leave the room
        if isinstance(room, bool):
            return room

    return 2  # Rat goes up to floor two


def second_floor():
    """
    Code to run the second floor

    :return: int floor - next floor number
    """
    pass


def third_floor():
    """
    Code to run the third floor

    :return: int floor - next floor number, str "Attic" for end
    """
    pass


def run_actions(floor, room, occupied, next):
    """
    Runs the choices that a rat can make 

    :return: str room that Rat goes into 
    """

    action = room_actions(room)
            
    ### While Player is not ready to move on ###
    while action != 4:
        reset_screen()
        ### Look for Rat Friends ###
        if action == 1:# No rat friends in room
            if not LOCATIONS[floor][room]["rats"]:
                print("There are no rat friends to be seen")
            else:
                rat = RAT_FRIENDS[LOCATIONS[1][room]["rats"][0]]
                
                # Rat friend too hidden
                if not hide(rat["Size"], PLAYER_RAT["stats"]["Vision"]):
                    print("{} can hear the familiar sound of one of their rat friends but".format(PLAYER_RAT["name"]))
                    print("they cannot see them in the room. Try searching again.")
                
                # Rat friend found
                else:
                    rat["Found"] = True

                    # Found Dumbo Rat Talon
                    if LOCATIONS[1][room]["rats"][0] == "Dumbo Rat Talon":
                        print("    A large Dumbo rat came out of his hiding place. {} recognized".format(PLAYER_RAT["name"]))
                        print('the rat as their friend Talon! "Hey pal," Talon greeted, "how is your')
                        print('Ratsgiving going?"')
                        print("    After {} explained their predicament, they asked if Talon wanted to".format(PLAYER_RAT["name"]))
                        print('come join Ratsgiving with them. "Sure! I would love to!" He enthusiastically')
                        print('responded. "Just don' + "'t let me get eaten by those mean cats. A big rat like")
                        print('me is always an easy target.')

                    # Found Hairless Rat Soron
                    elif LOCATIONS[1][room]["rats"][0] == "Hairless Rat Soron":
                        print("    A shivering small Hairless rat noticed {} looking at them and".format(PLAYER_RAT["name"]))
                        print("crawled out to reveal Soron. She hugged her front legs close to her body")
                        print('as she approached. "Hiya stranger" She greeted. "Long time no see. How' + "'s")
                        print('the family? What' + "'re y'all doing for Ratsgiving this time?" + '"')
                        print("    {} explained why they were still roaming the house and invited".format(PLAYER_RAT["name"]))
                        print('Soron to join them. "Why sure thing, sugar. I' + "'d love to spend Ratsgiving")
                        print("with y'all again! Just watch where ya going! My vision and balance ain't")
                        print('too good now."')

                    # Found Satin Rat Gemini
                    elif LOCATIONS[1][room]["rats"][0] == "Satin Rat Gemini":
                        print("    A shiny satin rat wiggled her whiskers and came out to greet")
                        print('{}. "Hey! Fancy catching you here! I thought you said you'.format(PLAYER_RAT["name"]))
                        print('had a Ratsgiving feast to get to!" Gemini squeaked.')
                        print("    {} explained what had happened and why they were not yet".format(PLAYER_RAT["name"]))
                        print('at the Ratsgiving feast. They invited Gemini to come join the')
                        print('festivities. "Of course! I' + "' love to come! Ratsgiving is always")
                        print('better enjoyed with friends!"')

                    # Found Tailless Rat Nellin
                    else:
                        print("    Nellin the scrawny tailless rat scampered out and noticed")
                        print('{}. "Hey partner. Whatcha still doing in these here halls?'.format(PLAYER_RAT["name"]))
                        print('Ya got a big family waiting for ya upstairs"')
                        print("    {} greeted Nellin and invited him to come along with".format(PLAYER_RAT["name"]))
                        print('them on this journey to get to the Ratsgiving feast. "Sure')
                        print("thing pal. I'd love to come with ya and see the folks again.")
                        print('been way too long."')
                    
                    rat_name = LOCATIONS[1][room]["rats"][0].split()[2]
                    
                    print(BANNER)
                    print("\x1B[3m" + "{} will now accompany you on the rest of your journey. Beware, if there is".format(rat_name) + "\x1B[0m")
                    print("\x1B[3m" + "a person or animal in the room you are moving into or out of, {}'s stats".format(rat_name) + "\x1B[0m")
                    print("\x1B[3m" + "will also be checked against the enemy. Try not to lose your friend." + "\x1B[0m")

        ### Look for Loot ###
        elif action == 2:
            total_count = sum([LOCATIONS[floor][room]["loot"][loot] for loot in LOCATIONS[floor][room]["loot"]])
            # If there is loot in the room
            if total_count != 0:
                found_loot = find(total_count)
                total_loot = []
                found_count = {
                    "stick": 0,
                    "seed": 0,
                    "cheese": 0,
                    "penny": 0,
                    "nickel": 0,
                    "dime": 0,
                    "quarter": 0
                }
                
                # Condensing all the loot in the room
                for loot in LOCATIONS[floor][room]["loot"]:
                    if LOCATIONS[floor][room]["loot"][loot] != 0:
                        for _ in range(LOCATIONS[floor][room]["loot"][loot]):
                            total_loot.append(loot)

                if not found_loot:
                    found_loot = 1

                # Finding a random amount of loot
                for _ in range(found_loot):
                    loot_choice = total_loot.pop(total_loot.index(choice(total_loot)))
                    LOCATIONS[floor][room]["loot"][loot_choice] -= 1
                    PLAYER_RAT["loot"][loot_choice] += 1
                    found_count[loot_choice] += 1

                # Printing found loot
                loot = ""
                for item in found_count:
                    if found_count[item] == 1:
                        loot += "    1 {}\n".format(item)

                    elif found_count[item] > 0:
                        if item == "penny":
                            term = "pennies"
                        else:
                            term = item + "s"

                        loot += "    {} {}\n".format(found_count[item], term)

                loot = loot[:-1]  # Remove \n character for formatting
                print("You have found the following loot:\n{}".format(loot))

                if found_loot != total_count:
                    print("\x1B[3m" + "You smell more loot in here. Try finding more" + "\x1B[0m")

            # If there is no loot in the room
            else:
                print("There seems to not be any loot in this room")

        ### Look into Next Room ###
        elif action == 3:
                print("Which room would you like to look into? ")


                for i in range(len(next)):
                    print("    {}: {}".format(i + 1, next[i]))
                
                room_choice = input("Please enter your selection: ")
                while not (room_choice.isdigit() and "1" <= room_choice <= str(len(next))):
                    print(SELECTION_ERROR)
                    room_choice = input("Please enter your selection: ")

                room_choice = int(room_choice) - 1

                # Printing occupants
                if next[room_choice] == "Ground Floor":
                    next_floor = 1
                    next_room = "Entryway"
                elif next[room_choice] == "Second Floor":
                    next_floor = 2
                    next_room = "Stair Landing"
                elif next[room_choice] == "Third Floor":
                    next_floor = 3
                    next_room = "Stair Landing"
                else:
                    next_floor = floor
                    next_room = next[room_choice]

                print_enemies(next_floor, next_room)
                
        ### View Map ###
        elif action == 5:
            print_map(floor)
                
        ### View Inventory ###
        else:
            inventory(PLAYER_RAT["loot"])

        action = room_actions(room)

    # Moving rooms
    print("Which room would you like to move into? ")
    
    for i in range(len(next)):
        print("    {}: {}".format(i + 1, next[i]))
    
    room_choice = input("Please enter your selection: ")
    while not (room_choice.isdigit() and "1" <= room_choice <= str(len(next))):
        print(SELECTION_ERROR)
        room_choice = input("Please enter your selection: ")

    room_choice = int(room_choice) - 1

    # Sets up for the next room 
    if next[room_choice] == "Ground Floor":
        next_floor = 1
        next_room = "Entryway"
    elif next[room_choice] == "Second Floor":
        next_floor = 2
        next_room = "Stair Landing"
    elif next[room_choice] == "Third Floor":
        next_floor = 3
        next_room = "Stair Landing"
    else:
        next_floor = floor
        next_room = next[room_choice]

    # Move enemies
    floors = ["Ground Floor", "Second Floor", "Third Floor"]
    enter = False

    print(BANNER)

    for character in ENEMIES:

        # Enemies have a 50% chance of moving
        if random() < .5:
            continue

        current_floor = ENEMIES[character]["Location"][0]
        current_room = ENEMIES[character]["Location"][1]
        next_move = CONNECTIONS[(current_floor,current_room)]

        if (current_floor == floor and current_room == room) or (current_floor == next_floor and current_room == next_room):
            print("    {} moves out of the {}".format(character, current_room))
            enter = True

        # Move Maids
        if "Maid" in character:
            current_room = choice([connection for connection in next_move if current_room in MAID_LOCATIONS[current_floor] or current_room in floors])
            if current_room in floors:
                if current_room == "Ground Floor":
                    current_room = "Entryway"
                    current_floor = 1
                elif current_room == "Second Floor":
                    current_room = "Stair Landing"
                    current_floor = 2
                else:
                    current_room = "Stair Landing"
                    current_floor = 3
            assign_room(current_floor, current_room, character)

        # Move Chefs
        elif "Chef" in character:
            current_room = choice([connection for connection in next_move if current_room in CHEF_LOCATIONS[current_floor]])
            assign_room(current_floor, current_room, character)

        # Move Butler
        elif "Butler" in character:
            current_room = choice([connection for connection in next_move if current_room in BUTLER_LOCATIONS[current_floor] or current_room in floors])
            if current_room in floors:
                if current_room == "Ground Floor":
                    current_room = "Entryway"
                    current_floor = 1
                elif current_room == "Second Floor":
                    current_room = "Stair Landing"
                    current_floor = 2
                else:
                    current_room = "Stair Landing"
                    current_floor = 3
            assign_room(current_floor, current_room, character)

        # Move Family
        elif "Hazelwood" in character:
            current_room = choice([connection for connection in next_move if current_room in FAMILY_LOCATIONS[current_floor] or current_room in floors])
            if current_room in floors:
                if current_room == "Ground Floor":
                    current_room = "Entryway"
                    current_floor = 1
                elif current_room == "Second Floor":
                    current_room = "Stair Landing"
                    current_floor = 2
                else:
                    current_room = "Stair Landing"
                    current_floor = 3
            assign_room(current_floor, current_room, character)

        # Move Cats
        else:
            current_room = choice([connection for connection in next_move if current_room in CAT_LOCATIONS[current_floor] or current_room in floors])
            if current_room in floors:
                if current_room == "Ground Floor":
                    current_room = "Entryway"
                    current_floor = 1
                elif current_room == "Second Floor":
                    current_room = "Stair Landing"
                    current_floor = 2
                else:
                    current_room = "Stair Landing"
                    current_floor = 3
            assign_room(current_floor, current_room, character)

        if (current_floor == floor and current_room == room) or (current_floor == next_floor and current_room == next_room):
            print("    {} moves into the {}".format(character, current_room))
            enter = True

    # User can see if enemies moved into or out of their current room and the room they are moving into
    if enter: 
        print(BANNER)  
        input("Hit ENTER to leave... ")

    # See if the enemies see the rat leaving
    if LOCATIONS[floor][room]["occupants"]:
        print("    As {} prepare to leave, they must make sure the enemies".format(PLAYER_RAT["name"]))
        print("do not spot them...")
        enter = detect(floor, room)
        if isinstance(enter, bool):
            return enter
        input("Hit ENTER to proceed into the {}... ".format(next_room))
    
    return next[room_choice]