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
from assets import BANNER
from display import reset_screen
from ChateauMap.map import FIRST_FLOOR
from ChateauMap.locations import LOCATIONS
from Statistics.rat_stats import PLAYER_RAT, RAT_FRIENDS
from GameScripts.movement import *

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


def print_first():
    """
    Prints the first floor map

    :return: None
    """
    print(BANNER, FIRST_LABEL, BANNER, ''.join(FIRST["map"]), BANNER, sep='\n')


### USED TO TEST LOCATION LABEL PLACEMENTS ###
# reset_map()
# for room in LOCATIONS[1]:
#     if room == "Entryway":
#         discover_entryway()
#     else:
#         discover_room(room, FIRST, 1)

#     print_first()
#     reset_first()


def first_floor():
    """
    Code to run the first floor

    :return: int floor - next floor number
    """
    room = "Entryway"

    while room != "Second Floor":
        reset_screen()
        next = FIRST_FLOOR.next_room
        occupied = True
        if room == "Entryway":
            if LOCATIONS[1][room]["found"]:  # If entryway was already found
                pass
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
                LOCATIONS[1][room]["rats"] = ["Hairless Rat Soron"]
                print("    Peering out from the hole in the wall into the Entryway of the")
                print("Chateau, the chandler hanging from the ceiling glimmers bright overhead.")
                print("Cautiously stepping forward, {} looks around.".format(PLAYER_RAT["name"]))
                
                if "Maid Alexander" in LOCATIONS[1][room]["occupants"]:
                    print("    Maid Alexander stood in the entryway, tiding up the entry console and")
                    print("table. He looks quite focused on his job.")
                elif "Maid Selina" in LOCATIONS[1][room]["occupants"]:
                    print("    Maid Selina is polishing the mirror hanging on one of the walls in the")
                    print("entryway. She has a duster next to her as well.")
                elif "Maid Sebastian" in LOCATIONS[1][room]["occupants"]:
                    print("    Maid Sebastian has a plethora of oddly shaped objects in their arms.")
                    print("They look as if they're working on reorganizing the entry table.")
                elif "Butler Apoorva" in LOCATIONS[1][room]["occupants"]:
                    print("    Butler Apoorva is waiting in the entryway for... something. {}".format(PLAYER_RAT["name"]))
                    print("does not know what. She is standing pretty stiffly near a wall.")
                elif "Mr. Hazelwood" in LOCATIONS[1][room]["occupants"]:
                    print("    Mr. Hazelwood rushes in with a wet umbrella. He looks annoyed")
                    print("and in a bit of a hurry.")
                elif "Mrs. Hazelwood" in LOCATIONS[1][room]["occupants"]:
                    print("    Mrs. Hazelwood takes off her heels and hangs her coat up on the coat")
                    print("rack. She drops her keys on to the entry table.")
                elif "Ms. Hazelwood" in LOCATIONS[1][room]["occupants"]:
                    print("    Little Ms. Hazelwood is sat on the floor of the entryway, fighting")
                    print("to get her boots off. Her cheeks are flushed from the cold.")
                else:
                    print(LOCATIONS[1][room]["occupants"])
                    occupied = False

        action = room_actions(room, occupied)

        ### While Player is not ready to move on ###
        while action != 4:
            ### Look for Rat Friends ###
            if action == 1:# No rat friends in room
                if not LOCATIONS[1][room]["rats"]:
                    print("There are no rat friends to be seen")
                else:
                    rat = RAT_FRIENDS[LOCATIONS[1][room]["rats"][0]]
                    
                    # Rat friend too hidden
                    if not hide(rat["Size"], PLAYER_RAT["stats"]["Size"]):
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
                            pass

                        # Found Tailless Rat Nellin
                        else:
                            pass
                        
                        rat_name = LOCATIONS[1][room]["rats"][0].split()[2]
                        
                        print(BANNER)
                        print("\x1B[3m" + "{} will now accompany you on the rest of your journey. Beware, if there is".format(rat_name) + "\x1B[0m")
                        print("\x1B[3m" + "a person or animal in the room you are moving into or out of, {}'s stats".format(rat_name) + "\x1B[0m")
                        print("\x1B[3m" + "will also be checked against the enemy. Try not to lose your friend." + "\x1B[0m")

            ### Look for Loot ###
            elif action == 2:
                pass

            ### Look into the next room ###
            elif action == 3:  
                pass

            ### View Map ###
            elif action == 5:
                pass

            ### View Inventory ###
            elif action == 6:
                pass

            ### Wait for enemies ###
            else:
                pass

            action = room_actions(room, occupied)
                

    return 2  # Rat goes up to floor two
