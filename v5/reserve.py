from settings import *
from item import *
import random

class Reserve:
    def __init__(self):
        # picked item indices, 0 = not picked, 1 = picked
        self.picked = [ 0 for _ in range(S.reserve_item_count) ]

        watchdog = 100000

        while True:
            self.items = []

            for _ in range(S.reserve_item_count):
                self.items.append(Item())

            # not all items are supposed to fit the sack
            if self.getTotalVolume() > S.sack_volume: break

            if not watchdog:
                print('Reserve could not create items enough in ' \
                      'quantity or in volume. Try with smaller sack_volume?')
                exit(1)

            watchdog -= 1

    def getTotalVolume(self):
        total_vol = 0

        for item in self.items: total_vol += item.volume

        return total_vol

    def pickRandom(self):
        while True:
            # lottery index
            index = random.randint(0, S.reserve_item_count - 1)
            # try another one if already picked
            if self.picked[index] == 1: continue

            self.picked[index] = 1

            return self.items[index]
        
    def pickBestRemaining(self, sack_space):
        fit_inds = []

        for i in range(S.reserve_item_count):

            # only select items not already marked taken
            if self.picked[i] == 1: continue

            # only select items that fit the sack
            if self.items[i].volume > sack_space: continue

            fit_inds.append(i)


        # amongst fit items, select the one with best value

        max_val = 0
        max_val_ind = None

        for i in fit_inds:
            if self.items[i].value > max_val:
                max_val = self.items[i].value
                max_val_ind = i

        if max_val_ind != None:
            self.picked[max_val_ind] = 1
            return self.items[max_val_ind]


    def returnToReserve(self, item):
        for i in range(S.reserve_item_count):

            # find matching item index (double checked with vol AND wgt)
            if item.volume == self.items[i].volume \
            and item.weight == self.items[i].weight:
                
                # toggle "item picked" to 0
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
