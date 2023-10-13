from item import *

class Sack:
    items = [] # sack contents, item objs + empty space
    volume = 0 # sack total item volume capacity
    space = volume # empty space left in the sack

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
        print(f'Total volume: {Sack.volume}')
        print(f'Space left: {Sack.space}')
        print(f'Space occupied: {Sack.volume - Sack.space}')
        print(f'Items total value: {Sack.getTotalValue()}')
        if Sack.items:
            print(f'Items:{Sack.itemsToString()}')

    def itemsToString():
        list_string = ''

        for item in Sack.items:
            list_string += f'\n  {item.toString()}'
        
        return list_string
