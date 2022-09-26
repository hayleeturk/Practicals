"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score < 50:
    result = "Bad"
elif score >= 90:
    result = "Excellent"
else:
    result = "Passable"
print("Result:", result)
