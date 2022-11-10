"""
CP1404 Practical 6
Guitars
Estimated time: 30 minutes
Actual time: 30 minutes
"""
import datetime

CURRENT_YEAR = datetime.datetime.now()  # Gets current date
VINTAGE_AGE = 50


class Guitar:
    """Represent Guitar class object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return data as a formatted f string"""
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        """Calculate age of guitar"""
        age = CURRENT_YEAR.year - self.year
        return age

    def is_vintage(self):
        """Determine if guitar is vintage"""
        if self.get_age() >= VINTAGE_AGE:
            return True

    def __lt__(self, other):
        """Sort guitars by year released"""
        return self.year < other.year
