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
from Statistics.rat_stats import PLAYER_RAT, RAT_FRIENDS
from display import reset_screen


def win_ending():
    """
    Prints the Win screen

    :return: bool Play Again
    """
    reset_screen()
    
    print("    After a long journey through the chateau, {} made it back safely".format(PLAYER_RAT["name"]))
    print("to the attic with", sep=" ")
    found_rats = [rat for rat in RAT_FRIENDS if RAT_FRIENDS[rat]["Found"]]

    if len(found_rats) > 1:
        print("Rat Friends", sep=" ")
        if len(found_rats) > 2: 
            for i in range(len(found_rats) - 1):
                print(found_rats[i] + ",", sep=" ")
        else:
            print(found_rats[0], sep=" ")
        print("and {}".format(found_rats[-1]))
    else:
        print("Rat Friend {}".format(found_rats[0]))

    print("    The family happily welcomed the late arrivals, especially since")
    print("{} bought a plentify bounty to the table. All's right in the world.")
    print("After all, it IS Ratsgiving.")
    print(BANNER)
    print("Congratulations on saving Ratsgiving, Player.")
    play = input("Would you like to play again [Y/N]? ")

    while play not in "yn" and play != "yes" and play != "no":
        if play != True:
            print(SELECTION_ERROR)
        play = input("Would you like to play again [Y/N]? ").lower()

    if play == "n" or play == "no":
        return False
    else:
        return True


def loss_ending(room, enemy, floor):
    """
    Prints the Lose screen

    :return: bool Play Again
    """
    reset_screen()
    print("    Unable to escape, {} was caught by {} in {} on".format(PLAYER_RAT["name"], enemy, room))
    print("the {} floor. The rat was placed in a cage and will be".format(floor))
    print("disposed of in the morning. Ratsgiving has been ruined.")
    print(BANNER)
    play = input("Would you like to try again [Y/N]? ")

    while play not in "yn" and play != "yes" and play != "no":
        if play != True:
            print(SELECTION_ERROR)
        play = input("Would you like to try again [Y/N]? ").lower()

    if play == "n" or play == "no":
        return False
    else:
        return True


def end_screen():
    """
    Prints the goodbye screen

    :return: None
    """
    reset_screen()
    print("We hope you enjoyed your stay at the Hazelwood Chateau! Hope to see you at the table again <3")
    print(BANNER)
    print(RAT)
