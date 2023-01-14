"""
CP1404 Practical 7
Project class
Estimated time: 30 minutes
Actual time: 20 minutes
"""


class Project:
    """Represent a project object."""

    def __init__(self, name="", date="", priority=0, cost=0.0, percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __str__(self):
        """Return data as a formatted f-string."""
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percentage}% "

    def __repr__(self):
        """Return representation of data as f-string."""
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percentage}%"

    def is_complete(self):
        """Return boolean for project completion."""
        return int(self.percentage) == 100

    def __lt__(self, other):
        """Sort projects by priority"""
        return self.priority < other.priority
