#!/usr/bin/env python3

"""
Provides enemy stats for a run

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from random import randint

ENEMIES = {
    "Mochi": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": "",
        "Description": ""
    },
    "Matcha": {
        "Speed": randint(10, 12),
        "Vision": randint(10, 12), 
        "Location": "",
        "Description": ""
    },
    "Maid Eleanor": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Maid Sabrina": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Maid Katherine": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Butler Apoorva": {
        "Speed": randint(6, 8),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Butler Benedict": {
        "Speed": randint(6, 8),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Chef Atwood": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Chef Marie": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Mrs. Hazelwood": {
        "Speed": randint(4, 6),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    }
    "Mr. Hazelwood": {
        "Speed": randint(6, 8),
        "Vision": randint(6, 8), 
        "Location": "",
        "Description": ""
    },
    "Ms. Hazelwood": {
        "Speed": randint(2, 4),
        "Vision": randint(4, 6), 
        "Location": "",
        "Description": ""
    }
}
CATS = ["Mochi", "Matcha"]
MAIDS = [enemy for enemy in ENEMIES if "Maid" in enemy]
PLACEMENTS = {
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
        "Game Room": [],
    },
    3: {
        "Stair Landing": [],
        "Master Bedroom": [],
        "Ensuite Bathroom": [],
        "Office": [],
        "Rat Hole": [],
    }
}


def move_enemies():
    level_one = {}
    level_two = {}