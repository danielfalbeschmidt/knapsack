import random
from measure import *

class Item:
    def __init__(self):
        self.volume = random.random()
        self.weight = random.random()
        self.value =  self.weight * self.volume
        self.volume_category = self.setCategory(self.volume)
        self.weight_category = self.setCategory(self.weight)

    def toString(self):
        return f'volume: {self.volume_category}, '\
            f'weight: {self.weight_category}'
    
    def setCategory(self, measure):
        if measure < 1 / 3: return 1
        if measure < 2 / 3: return 2
        return 3