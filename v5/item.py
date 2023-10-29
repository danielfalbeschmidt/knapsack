import random

class Item:
    def __init__(self):
        self.volume = random.random()
        self.weight = random.random()
        self.value =  self.weight * self.volume
        