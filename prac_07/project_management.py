"""
CP1404 Practical 7
Project management program
Estimated time:
Actual time:
"""

import datetime

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit "


def main():
    """Add DOCSTRIGN"""
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            pass
        elif menu_choice == "S":
            pass
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        print(MENU)
    menu_choice = input(">>>").upper()
