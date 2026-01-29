import random

class DisasterEnvironment:
    def __init__(self):
        self.severity = 0

    def get_severity(self):
        # Simulate changing conditions with a random walk
        change = random.choice([-1, 0, 1, 2])
        self.severity = max(0, min(10, self.severity + change))
        return self.severity
