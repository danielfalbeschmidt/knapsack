import random

class Item:
    def __init__(self):
        self.weight = random.random()
        self.volume = random.random()
        self.value =  self.weight * self.volume

    def toString(self):
        return f'volume: {round(self.volume, 3)}, weight: {round(self.weight, 3)}'
    