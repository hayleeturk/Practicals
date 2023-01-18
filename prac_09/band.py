"""CP1404 Practical 9 - Band class"""


class Band:
    """Represent a band object."""

    def __init__(self, name=""):
        """Initialise a band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band object."""
        return f"{self.name} ({' '.join([str(musician) for musician in self.musicians])})"

    def add(self, musician):
        """Add a musician to musicians."""
        self.musicians.append(musician)

    def play(self):
        """Returns musicians and instruments details."""
        for musician in self.musicians:
            play = musician.play()
        return play
