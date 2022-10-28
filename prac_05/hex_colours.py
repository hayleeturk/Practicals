"""
CP1404 Practical
Hexadecimal colour codes
Estimated time:
Actual time:
"""

hexadecimal_to_colour = {"asparagus": "#87a96b", "banana yellow": "#ffe135", "camel": "#c19a6b",
                         "dogwood rose": "#d71868", "ebony": "#555d50", "eggplant": "#614051",
                         "eggshell": "#f0ead6", "fuzzy wuzzy": "#87421f", "green lizard": "#a7f432",
                         "macaroni and cheese": "#ffbd88", "piggy pink": "#fddde6", "razzmatazz": "#e3256b"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in hexadecimal_to_colour:
        print(f"{colour_name} is {hexadecimal_to_colour[colour_name]}")
    else:
        print("Invalid colour!")
    colour_name = input("Enter colour name: ").lower()
print("Finished")
