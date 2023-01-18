"""CP1404 Practical 9 - Silver Service Taxi"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Version of a taxi with a higher price per km."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance, inherited from class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get silver fare."""
        return self.flagfall + super().get_fare()
