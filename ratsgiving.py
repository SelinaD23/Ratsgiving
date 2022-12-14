#!/usr/bin/env python3

"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from importlib import reload
from Components.assets import *
from Components.GameScripts.start import start
from Components.end_screen import end_screen, win_ending
from Components.GameScripts.reset_game import reset_map
from Components.GameScripts.chateau import first_floor, second_floor, third_floor
import Components.Statistics.rat_stats as rat_stats
import Components.Statistics.enemies as enemies

def main():
    play = True
    loss = False

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

            if floor == True or floor == False:
                loss = True
                play = floor

        if not loss:
            play = win_ending()

        reload(rat_stats)
        reload(enemies)

    end_screen()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end_screen()
