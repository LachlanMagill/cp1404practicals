"""estimated time 10 min
started at 2:21pm
finished at 2:33pm
total time 12min"""
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
