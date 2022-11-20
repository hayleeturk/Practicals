"""
CP1404 Practical 7
Project management program
Estimated time:
Actual time:
"""

from prac_07.project import Project
import datetime

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit "
FILENAME = "projects.txt"


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
            display_projects(FILENAME)
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        print(MENU)
        menu_choice = input(">>>").upper()
    print("Finished")


def display_projects(filename):
    project = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        name = parts[0]
        date = parts[1]
        priority = parts[2]
        cost = parts[3]
        percentage = parts[4]
        my_project = Project(name, date, priority, cost, percentage)
        project.append(my_project)
    print(project)
    in_file.close()






main()
