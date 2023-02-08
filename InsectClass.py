import random


class Insect:
    def __init__(self):
        self.flight = ""
        self.wings = "2"
        self.legs = "4"

    def flight(self):
        for random.randint in range(10):
            self.flight = random.randint

    def get_length(self):
        return self.flight
