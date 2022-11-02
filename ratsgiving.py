#!/usr/bin/env python3

"""
Runs a text based game named Ratsgiving

Programmed by: Selina Ding
https://github.com/SelinaD23
"""

from assets import *
from start import start
from importlib import reload
from end_screen import end_screen
from display import reset_screen
import rat_stats
import enemies

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
