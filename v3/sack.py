from settings import *
from item import *

class Sack:
    def __init__(self):
        self.volume = Settings.sack_volume
        self.space = self.volume # empty space left in the sack
        self.items = [] # sack contents: item objs + empty space

    def add(self, item):
        if item.volume > self.space: return
        
        self.space -= item.volume
        self.items.append(item)
        return True

    def getTotalVolume(self):
        total = 0

        for item in self.items:
            total += item.volume

        return total

    def getTotalWeight(self):
        total = 0

        for item in self.items:
            total += item.weight

        return total

    def getTotalValue(self):
        total = 0

        for item in self.items:
            total += item.value

        return total
    
    def sortItemsByVolume(self):
        sorted_items = []
        moved_item = self.items.pop()
        sorted_items.append(moved_item)

        while self.items:
            moved_item = self.items.pop()

            for index in range(len(sorted_items)):
                if moved_item.volume < sorted_items[index].volume:
                    sorted_items.insert(index, moved_item)
                    break

            else: sorted_items.insert(len(sorted_items), moved_item)

        self.items = sorted_items
    
    def printDetails(self):
        print('*** SACK ***')
        print(f'Total volume: {round(self.volume, 3)}')
        print(f'Space left: {round(self.space, 3)}')
        print(f'Space occupied: {round(self.volume - self.space, 3)}')
        print(f'Items total value: {round(self.getTotalValue(), 3)}')
        print(f'Distributions [volumes 3, weights 3]: {self.getVolumeDistributions()}')
        print(f'Item category values: {self.itemsToString()}\n')

    def itemsToString(self):
        list_string = ''

        for item in self.items:
            list_string += f'\n  {item.toString()}'
        
        if not list_string: return ' No items'
        return list_string
