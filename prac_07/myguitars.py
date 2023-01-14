"""
CP1404 Practical 7
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to read from file and store data in list using class."""
    my_guitars = []
    with open(FILENAME, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")  # Split data at ","
            name = parts[0]
            year = parts[1]
            cost = parts[2]
            my_guitar = Guitar(name, year, cost)
            my_guitars.append(my_guitar)
        get_new_guitar(my_guitars)
        my_guitars.sort()
        print(my_guitars)
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        for guitar in my_guitars:
            print(guitar.name, guitar.year, guitar.cost, sep=",", file=out_file)


def get_new_guitar(my_guitars):
    """Take user input for new guitar object"""
    name = input("Name: ")
    while name != "":
        age = get_valid_number("Age: ")
        price = get_valid_number("Price: ")
        new_guitar = Guitar(name, age, price)
        my_guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")


def get_valid_number(prompt):
    """Get a valid number from user with error checking."""
    number = input(prompt)
    while number == "":
        print("Please enter a number")
        number = input(prompt)
    return number


if __name__ == "__main__":
    main()
