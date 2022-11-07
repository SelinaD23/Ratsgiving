#!/usr/bin/env python3

"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from importlib import reload
from Components.assets import *
from Components.GameScripts.start import start
from Components.end_screen import end_screen, determine_ending
from Components.GameScripts.reset_game import reset_map
from Components.GameScripts.first_floor import first_floor
from Components.GameScripts.second_floor import second_floor
from Components.GameScripts.third_floor import third_floor
import Components.Statistics.rat_stats as rat_stats
import Components.Statistics.enemies as enemies

def main():
    play = True

    while play:
        reset_map()
        start()
        floor = 1
        while floor != "Attic":
            if floor == 1:
                floor = first_floor()
            elif floor == 2:
                floor = second_floor()
            else:
                floor = third_floor()

        determine_ending()

        while play not in "yn" and play != "yes" and play != "no":
            if play != True:
                print(SELECTION_ERROR)
            play = input("Would you like to play again [Y/N]? ").lower()

        if play == "n" or play == "no":
            end_screen()

        reload(rat_stats)
        reload(enemies)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end_screen()
