"""
CP1404 Practical
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_PICK = 6
MINIMUM = 1
MAXIMUM = 45

number_of_picks = int(input("How many picks?: "))
while number_of_picks < 1:
    print("Invalid number!")
    number_of_picks = int(input("How many picks?: "))

for i in range(number_of_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_PICK):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in quick_picks:
            random_number = random.randint(MINIMUM, MAXIMUM)
        quick_picks.append(random_number)
    print(" ".join(f"{random_number:2}" for random_number in sorted(quick_picks)))

