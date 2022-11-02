#!/usr/bin/env python3

"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from importlib import reload
from Components.assets import *
from Components.GameScripts.start import start
from Components.end_screen import end_screen
from Components.display import reset_screen
import Components.Statistics.rat_stats as rat_stats
import Components.Statistics.enemies as enemies

def main():
    play = True

    while play:
        name, breed = start()


        reload(rat_stats)
        reload(enemies)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        reset_screen()
        end_screen()
