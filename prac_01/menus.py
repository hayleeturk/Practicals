"""
CP1404/CP5632 - Practical
Simple program to display menu options
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Name: ").title()
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
