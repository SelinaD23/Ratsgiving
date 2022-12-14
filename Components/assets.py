#!/usr/bin/env python3

"""
Art Assets for Ratsgiving Game

https://github.com/SelinaD23
"""

# Rat credits: Joan Stark
RAT = """         __             _,-"~^"-.
       _// )      _,-"~`         `.
     ." ( /`"-,-"`                 ;
    / 6                             ;
   /           ,             ,-"     ;
  (,__.--.      \           /        ;
   //'   /`-.\   |          |        `._________
     _.-'_/`  )  )--...,,,___\     \-----------,)
   ((("~` _.-'.-'           __`-.   )         //
     jgs ((("`             (((---~"`         //
                                            ((________________
                                            `----""""~~~~^^^```"""

# Title generated from https://fsymbols.com/generators/carty/
TITLE = """ ██████╗░░█████╗░████████╗░██████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░██████╗░
 ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝░██║██║░░░██║██║████╗░██║██╔════╝░
 ██████╔╝███████║░░░██║░░░╚█████╗░██║░░██╗░██║╚██╗░██╔╝██║██╔██╗██║██║░░██╗░
 ██╔══██╗██╔══██║░░░██║░░░░╚═══██╗██║░░╚██╗██║░╚████╔╝░██║██║╚████║██║░░╚██╗
 ██║░░██║██║░░██║░░░██║░░░██████╔╝╚██████╔╝██║░░╚██╔╝░░██║██║░╚███║╚██████╔╝
 ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░"""

BANNER = "============================================================================="

SELECTION_ERROR = "    ERROR: Selection invalid"

MAP_ART = {
  "First Empty": list("""                            _______
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
    |_______|______________________|__________|"""), 
    "First Full": """                            _______
                           |Laundry|
                           | Room  |
     ___x__________________|__/ \__|__________
    |       |          |  Servant  |          |
    |   E   | Bathroom |   Room   \  Kitchen  |
    |   n   |____/_____|___________|___/ \____|
    |   t   |                      |          |
    |   r    /       Hallway        /         |
    |   y   |__________/ \_________|  Dining  |
    |   w   |                      |   Room   |
    |   a    /     Living Room      /         |
    |   y   |                      |          |
    |_______|______________________|__________|""", 
    "Second Empty": list("""     _______ _________________________________
    |       |          |                      |
    |       |           /                     |
    |       |          |                      |
    |       |____/_____|_____/_____           |
    |                              |          |
    |        ___________\___/______|__________|
    |       |             |                   |
    |       |             |                   |
    |       |             |                   |
    |_______|_____________|___________________|"""), 
    "Second Full": """     _______ _________________________________
    |       |          |                      |
    |     L | Bathroom  /  Ms. Hazelwood's    |
    |  S  a |          |       Bedroom        |
    |  t  n |____/_____|_____/_____           |
    |  a  d                        |          |
    |  i  i  ___________\___/______|__________|
    |  r  n |             |                   |
    |     g |    Game     |      Theater      |
    |       |    Room     |       Room        |
    |_______|_____________|___________________|""",
    "Third Empty": list("""     _______ ______________________
    |       |          |           |
    |       |          |           |
    |        /         |           |
    |       |__________|_____/_____|
    |       |                      |
    |       |                      |
    |        /                      |
    |       |                      |
    |       |                      |
    |_______|______________________|"""), 
    "Third Full": """     _______ ____________________o_
    |       |          |           |
    |     L |  Office  |  Ensuite  |
    |  S  a  /         |  Bathroom |
    |  t  n |__________|_____/_____|
    |  a  d |                      |
    |  i  i |                      |
    |  r  n  /       Master        |
    |     g |       Bedroom        |
    |       |                      |
    |_______|______________________|"""
}


### USED TO DETERMINE WHERE LOCATIONS LABELS ARE ###
# floor = "Third Full"
# for index in range(len(MAP_ART[floor])):
#     if MAP_ART[floor][index].isalpha():
#         print(index, MAP_ART[floor][index])
