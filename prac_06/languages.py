"""
Cp1404 Practical 6
Create programming language class
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing=bool, reflection="", year=0):
        """Initiate programming language class objects"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return data as a string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language typing is dynamic"""
        if self.typing == "Dynamic":
            return True
