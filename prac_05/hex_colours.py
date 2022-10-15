"""
CP1404 Practical
Hexadecimal colour codes
"""

hexadecimal_to_colour = {"Asparagus": "#87a96b", "Banana Yellow": "#ffe135", "Camel": "#c19a6b",
                         "Dogwood Rose": "#d71868", "Ebony": "#555d50", "Eggplant": "#614051",
                         "Eggshell": "#f0ead6", "Fuzzy Wuzzy": "#87421f", "Green Lizard": "#a7f432",
                         "Macaroni and Cheese": "#ffbd88", "Piggy Pink": "#fddde6", "Razzmatazz": "#e3256b"}

colour_name = str(input("Enter colour name: ").title())
while colour_name != "":
    if colour_name in hexadecimal_to_colour:
        print(f"{colour_name} is {hexadecimal_to_colour[colour_name]}")
    else:
        print("Invalid colour!")
    colour_name = str(input("Enter colour name: ").title())
print("Finished")
