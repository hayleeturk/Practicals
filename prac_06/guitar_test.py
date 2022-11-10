"""
CP1404 Practical 6
Guitar class testing
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def run_tests():
    """Testing for guitar clss"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    print(f"{guitar.name} - Expected 100. Got {guitar.get_age()}")

# Gibson L-5 CES get_age() - Expected 100. Got 100
# Another Guitar get_age() - Expected 9. Got 9
# Gibson L-5 CES is_vintage() - Expected True. Got True
# Another Guitar is_vintage() - Expected False. Got False


if __name__ == '__main__':
    run_tests()
