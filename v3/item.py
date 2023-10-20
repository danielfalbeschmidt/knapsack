from settings import *
import random

class Item:
    def __init__(self):
        self.volume = random.random()
        self.weight = random.random()

        self.volume_category = int(self.volume * S.volume_category_count)
        self.weight_category = int(self.weight * S.volume_category_count)

        self.value =  self.weight * self.volume

    def toString(self):
        return f'volume category: {self.volume_category}, '\
            f'weight category: {self.weight_category}'