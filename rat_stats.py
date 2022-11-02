#!/usr/bin/env python3

"""
Provides rat stats for a run

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from assets import *
from random import randint

BREEDS = {
    "Standard": {
        "Size": randint(5, 8),
        "Speed": randint(5, 8),
        "Vision": randint(5, 8),
        "Balance": randint(5, 8),
        "Hearing": randint(5, 8)
    },
    "Rex": {
        "Size": randint(5, 8),
        "Speed": randint(5, 8),
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": randint(9, 12)
    },
    "Satin": {
        "Size": randint(1, 4),
        "Speed": randint(9, 12),
        "Vision": randint(1, 4),
        "Balance": randint(5, 8),
        "Hearing": randint(5, 8)
    },
    "Dumbo": {
        "Size": randint(9, 12),
        "Speed": randint(1, 4),
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": randint(9, 12)
    },
    "Tailless": {
        "Size": randint(1, 4),
        "Speed": randint(1, 4),
        "Vision": randint(9, 12),
        "Balance": randint(1, 4),
        "Hearing": randint(9, 12)
    },
    "Hairless": {
        "Size": randint(1, 4),
        "Speed": randint(9, 12),
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": randint(9, 12)
    },
    "Bristle Coat": {
        "Size": randint(9, 12),
        "Speed": randint(9, 12),
        "Vision": randint(1, 4),
        "Balance": randint(1, 4),
        "Hearing": randint(5, 8)
    }
}
BREED_NUMS = {
    1: "Standard",
    2: "Rex",
    3: "Satin",
    4: "Dumbo",
    5: "Tailless",
    6: "Hairless",
    7: "Bristle Coat"
}
SPACES = 4 * 6


def print_breeds():
    print("SELECT YOUR BREED: (STAT VALUES: 1 - Lowest, 12 - Highest)")
    print(BANNER)

    # Local variables to be used in loop
    stats = ["Name", "Size", "Speed", "Vision", "Balance", "Hearing"]
    breeds = [["Standard [1]", "Rex [2]", "Satin [3]"],
              ["Dumbo [4]", "Tailless [5]", "Hairless [6]", "Bristle Coat [7]"]]

    # Printing out the breed menu
    for i in range(len(breeds)):
        for stat in stats:
            if stat == "Name":
                for breed in breeds[i]:
                    # This code was used for formatting
                    breed_str = " " * 4 + stat + ": " + breed
                    if breed != "Bristle Coat [7]":  # Bristle Coat was too long and at the end so I ignored
                        breed_str += " " * (SPACES - len(breed_str))
                    print(breed_str, end="")
            else:
                for breed in breeds[i]:
                    breed = breed[:-4]  # Removes the [#] attached to the end of the string
                    # This code was used for formatting
                    stat_str = " " * 8 + stat + ": " + str(BREEDS[breed][stat])
                    stat_str += " " * (SPACES - len(stat_str))
                    print(stat_str, end="")
            print()

    print(BANNER)
