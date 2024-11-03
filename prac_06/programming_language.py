"""estimated time 20 min
started at 2 pm
finished at 2:13pm
total time 13 min"""

class ProgrammingLanguage:
    """Represent a programming language with its characteristics."""

    def __init__(self, name, typing, reflection, year):
        """Initialize the attributes of the programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
