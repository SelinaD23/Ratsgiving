#!/usr/bin/env python3

"""
End screens for Ratsgiving game

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from assets import *
from Statistics.rat_stats import PLAYER_RAT
from display import reset_screen


def determine_ending():
    pass


def end_screen():
    """
    Prints the goodbye screen

    :return: None
    """
    reset_screen()
    print("We hope you enjoyed your stay at the Hazelwood Chateau! Hope to see you at the table again <3")
    print(BANNER)
    print(RAT)
