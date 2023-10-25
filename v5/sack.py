from settings import *
from item import *

class Sack:
    def __init__(self):
        self.volume = S.sack_volume
        self.space = self.volume # empty space left in the sack
        self.items = [] # sack contents: item objs + empty space

    def add(self, item):
        if not item or item.volume > self.space: return
        
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

    def itemsToString(self):
        list_string = ''

        for item in self.items:
            list_string += f'\n  {item.toString()}'
        
        if not list_string: return ' No items'
        return list_string
