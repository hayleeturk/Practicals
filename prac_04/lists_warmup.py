"""
CP1404 Practical
"""

# Warm-up

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3, 1, 4, 1, 5, 9
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change first element to "ten"
del numbers[0]
numbers = ["ten"] + numbers
print(numbers)

# Change last element to 1
del numbers[-1]
numbers = numbers + [1]
print(numbers)

# Print all except first two
print(numbers[2:-1])

if 9 in numbers:
    print("9 is an element in numbers")
else:
    print("9 is not an element in numbers")


