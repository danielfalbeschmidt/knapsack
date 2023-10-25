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

    def getItemVolumeSum(self, picks):
        s = 0

        for i in range(S.reserve_item_count):
            if round(picks[i]): s += self.items[i].volume

        return s

    def getItemWeightSum(self, picks):
        s = 0

        for i in range(S.reserve_item_count):
            if round(picks[i]): s += self.items[i].weight

        return s

    def getItemValueSum(self, picks):
        s = 0

        for i in range(S.reserve_item_count):
            if round(picks[i]): s += self.items[i].volume * self.items[i].weight

        return s

    def getWeightToVolumeSum(self, picks):
        s = 0

        for i in range(S.reserve_item_count):
            if round(picks[i]): s += self.items[i].weight / self.items[i].volume

        return s

    def printDetails(self):
        print('*** RESREVE ***')

        print('Items:')
        for item in self.items:
            print(f'\tvolume:\t{round(item.volume, 3)}', end='\t')
            print(f'\tweight:\t{round(item.weight, 3)}', end='\t')
            print(f'\tvalue:\t{round(item.value, 3)}', end='\t')
            print(f'\tweight / volume:\t{round(( item.weight / item.volume ), 3)}')
