"""
CP1404 Practical
Program with functions to
get score and print stars
"""

MENU = "(R)esult\n(P)rint stars\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        score = get_valid_score()
        if choice == "R":
            result = determine_result(score)
            print("Result: ", result)
        elif choice == "P":
            stars = get_stars(score)
            print(stars)
        else:
            print("Invalid menu option")
        print(MENU)
        choice = input(">>>").upper()
    print("Finished")



 # score = get_valid_score()
 #        result = determine_result(score)
 #        stars = get_stars(score)
 #        print(f"Result: {result}\n{stars}")




def get_valid_score():
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score (0-100): "))
    return score


def determine_result(score):
    if score < 50:
        result = "Bad"
    elif score >= 90:
        result = "Excellent"
    else:
        result = "Passable"
    return result


def get_stars(score):
    stars = score * "*"
    return stars


main()
