from item import *

class Sack:
    items = [] # sack contents, item objs + empty space
    volume = 0 # sack total item volume capacity
    space = volume # empty space left in the sack

    def empty():
        Sack.items = []
        Sack.space = Sack.volume

    def setVolume(volume=4):
        Sack.volume = volume
        Sack.space = volume

    def add(item):
        if item.volume > Sack.space: return
        
        Sack.space -= item.volume
        Sack.items.append(item)
        return True

    def getTotalValue():
        total = 0

        for item in Sack.items:
            total += item.value

        return total
    
    def printDetails():
        print('*** SACK ***')
        print(f'Total volume: {round(Sack.volume, 3)}')
        print(f'Space left: {round(Sack.space, 3)}')
        print(f'Space occupied: {round(Sack.volume - Sack.space, 3)}')
        print(f'Items total value: {round(Sack.getTotalValue(), 3)}')
        print(f'Items:{Sack.itemsToString()}\n')

    def itemsToString():
        list_string = ''

        for item in Sack.items:
            list_string += f'\n  {item.toString()}'
        
        if not list_string: return ' No items'
        return list_string
