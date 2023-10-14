import random
from size import *

class Item:
    def __init__(self):
        self.weight = random.random()
        self.volume = random.random()
        self.value =  self.weight * self.volume
        self.category = None

    def toString(self):
        return f'volume: {round(self.volume, 3)}, '\
            f'weight: {round(self.weight, 3)}, '\
            f'category: {Size.toString(self.category)}'
    