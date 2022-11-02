#!/usr/bin/env python3

"""
Handles the print of the display

Programmed by: Selina Ding
https://github.com/SelinaD23
"""
from os import system, name
from Components.assets import *


def reset_screen():
    """
    Clears the terminal and outputs the Ratsgiving title card

    :return: None
    """
    system('clear' if name == 'posix' else 'CLS')
    print(BANNER)
    print(TITLE)
    print(BANNER)