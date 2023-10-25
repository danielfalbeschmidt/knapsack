from settings import *
from item import *
import random

class Reserve:
    def __init__(self):
        self.items = []
        self.picked = [] # picked item indices, 0 = not picked, 1 = picked

        while True:
            for _ in range(S.reserve_item_count):
                self.items.append(Item())

            if self.getTotalVolume() > S.sack_volume: break

        for _ in range(S.reserve_item_count):
            self.picked.append(0)

    def getTotalVolume(self):
        total_vol = 0

        for item in self.items:
            total_vol += item.volume

        return total_vol

    def pickRandom(self):
        if 0 not in self.picked: return

        while True:
            index = random.randint(0, S.reserve_item_count - 1)
            
            if self.picked[index] == 1: continue

            self.picked[index] = 1

            return self.items[index]
        
    def pickSmallestVolume(self):
        min_vol = 1
        min_ind = None

        for i in range(S.reserve_item_count):
            if self.picked[i] == 1: continue

            if self.items[i].volume < min_vol:
                min_ind = i
                min_vol = self.items[i].volume

        if min_ind: return self.items[min_ind]
