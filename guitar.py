"""
CP1404 Practical 6
Guitars
Estimated time: 30
Actual time:
"""

CURRENT_YEAR = 2022


class Guitar:
    """Represent Guitar class object"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return data as a formatted f string"""
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        """Calculate age of guitar"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self, age):
        """Determine if guitar is vintage (older than 50 years)"""
        if age > 50:
            return True

