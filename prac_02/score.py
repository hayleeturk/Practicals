"""
CP1404 Practical
Program to determine score status
refactored to include functions
"""

import random


def main():
    score = get_score()
    result = determine_result(score)
    print("Result:", result)
    random_score = get_random_score()
    result = determine_result(random_score)
    print(f"Randomly generated score: {random_score} \nResult: {result}")


def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    if score < 50:
        result = "Bad"
    elif score >= 90:
        result = "Excellent"
    else:
        result = "Passable"
    return result


def get_random_score():
    random_score = random.randint(0, 100)
    return random_score


main()
