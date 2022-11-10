"""
CP1404 Practical 6
Guitars program
Estimated time: 20 minutes
Actual time:35 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Program to store guitar data using classes."""
    my_guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ")
        cost = get_valid_number("Cost: ")
        guitar_data = Guitar(name, year, cost)
        my_guitars.append(guitar_data)
        print(guitar_data, "added.")
        name = input("Name: ")
    if my_guitars:
        my_guitars.sort()
        print("These are my guitars:")
        vintage_string = ""
        for i, guitar in enumerate(my_guitars, 1):
            vintage_string = determine_if_vintage(guitar)
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars. Quick, go and buy one!")


def get_valid_number(prompt):
    """Get a valid number from user."""
    number = float(input(prompt))
    while number < 1:
        print("Invalid number")
        number = float(input(prompt))
    return number


def determine_if_vintage(guitar):
    """Return vintage string if guitar is vintage."""
    if guitar.is_vintage():
        return "(vintage)"
    return ""


if __name__ == '__main__':
    main()
