from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)  # Ensure priority is stored as an integer
        self.cost_estimate = float(cost_estimate)  # Ensure cost_estimate is stored as a float
        self.completion_percentage = int(completion_percentage)  # Ensure completion_percentage is stored as an integer

    def is_complete(self):
        return self.completion_percentage == 100  # Return True if the project is complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
