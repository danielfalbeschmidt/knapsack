from settings import *
from item import *

class Sack:
    def __init__(self):
        self.volume = S.sack_volume
        self.space = self.volume # empty space left in the sack
        self.items = [] # sack contents, item objs

    def add(self, item):
        if item.volume > self.space: return
        
        self.space -= item.volume
        self.items.append(item)
        
        return True

    def getTotalVolume(self):
        total = 0

        for item in self.items: total += item.volume

        return total

    def getTotalWeight(self):
        total = 0

        for item in self.items: total += item.weight

        return total

    def getTotalValue(self):
        total = 0

        for item in self.items: total += item.value

        return total

    def printDetails(self):
        print('*** SACK ***')

        print(f'Total sack volume: {S.sack_volume}')
        print(f'Total items volume: {self.getTotalVolume}')
        print(f'Empty space left: {self.space}')
        print(f'Total items weight: {self.getTotalWeight}')
        print(f'Total items value: {self.getTotalValue}')
