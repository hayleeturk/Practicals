"""CP1404 Practical 9 - Unreliable Car"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable version of a Car."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent car but only if reliability > random integer."""
        if self.reliability > random.randint(0, 100):
            return super().drive(distance)
        return 0




