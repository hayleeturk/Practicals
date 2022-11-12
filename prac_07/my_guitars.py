"""
CP1404 Practical
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to read from file and store data in list using class."""
    in_file = open(FILENAME, "r")
    my_guitars = []
    for line in in_file:
        parts = line.strip().split(",")  # Split data at ","
        name = parts[0]
        year = parts[1]
        cost = parts[2]
        my_guitar = Guitar(name, year, cost)
        my_guitars.append(my_guitar)
    in_file.close()

    for my_guitar in my_guitars:  # testing
        print(my_guitar)


if __name__ == "__main__":
    main()
