from settings import *
from item import *
import random

class Reserve:
    def __init__(self):
        self.picked = [] # picked item indices, 0 = not picked, 1 = picked

        while True:
            self.items = []

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
        while True:
            index = random.randint(0, S.reserve_item_count - 1)
            
            if self.picked[index] == 1: continue

            self.picked[index] = 1

            return self.items[index]
        
    def pickBestRemaining(self, sack_space):
        fit_inds = []

        for i in range(S.reserve_item_count):
            if self.picked[i] == 1: continue
            if self.items[i].volume > sack_space: continue

            fit_inds.append(i)

        max_val = 0
        max_val_ind = None

        for i in fit_inds:
            if self.items[i].value > max_val:
                max_val = self.items[i].value
                max_val_ind = i

        if max_val_ind != None:
            self.picked[max_val_ind] = 1
            return self.items[max_val_ind]


    def returnItem(self, item):
        for i in range(S.reserve_item_count):
            if item.volume == self.items[i].volume \
            and item.weight == self.items[i].weight:
                self.picked[i] = 0
                return

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

        print(f'Volume sum: {round(self.getItemVolumeSum( [ 1 for _ in range(S.reserve_item_count) ] ), 3)}')

        print('Items:')
        for item in self.items:
            print(f'\tvolume:\t{round(item.volume, 3)}', end='\t')
            print(f'\tweight:\t{round(item.weight, 3)}', end='\t')
            print(f'\tvalue:\t{round(item.value, 3)}', end='\t')
            print(f'\tweight / volume:\t{round(( item.weight / item.volume ), 3)}')
