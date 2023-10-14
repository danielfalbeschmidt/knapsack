from item import *
from size import *

class Reserve:
    count = 0 # total number of created items
    total_volume = 0

    small = [] # item volume categories
    medium = []
    large = []

    def reset():
        Reserve.total_volume = 0

        Reserve.small = [] # item volume categories
        Reserve.medium = []
        Reserve.large = []

    def create(count=9):
        Reserve.count = count
        items = Reserve.populate()
        Reserve.total_volume = Reserve.getTotalVolume(items)        
        sorted_items = Reserve.sortByVolume(items)
        Reserve.categorize(sorted_items)

    def populate():
        items = []

        for _ in range(Reserve.count):
            items.append(Item())

        return items
    
    def sortByVolume(items):
        sorted_items = []
        moved_item = items.pop()
        sorted_items.append(moved_item)

        while items:
            moved_item = items.pop()

            for index in range(len(sorted_items)):
                if moved_item.volume > sorted_items[index].volume: continue

                sorted_items.insert(index, moved_item)
                break

            else: sorted_items.insert(len(sorted_items), moved_item)

        return sorted_items


    def categorize(sorted_items):
        iterator = range(int(Reserve.count / 3))
        index = 0
        
        for _ in iterator:
            sorted_items[index].category = Size.SMALL
            Reserve.small.append(sorted_items[index])
            index += 1
        
        for _ in iterator:
            sorted_items[index].category = Size.MEDIUM
            Reserve.medium.append(sorted_items[index])
            index += 1

        while index < Reserve.count:
            sorted_items[index].category = Size.LARGE
            Reserve.large.append(sorted_items[index])
            index += 1

    def getTotalVolume(items):
        total = 0

        for item in items:
            total += item.volume

        return total

    def printDetails():
        print('*** RESERVE ***')
        print(f'Reserve total volume: {round(Reserve.total_volume, 3)}')
        print('Reserve item volumes by categories:')
        print(f'  Small:  {Reserve.itemsToString(Reserve.small)}')
        print(f'  Medium: {Reserve.itemsToString(Reserve.medium)}')
        print(f'  Large:  {Reserve.itemsToString(Reserve.large)}\n')

    def itemsToString(list):
        list_string = ''

        for item in list:
            list_string += f' {round(item.volume, 3)}'
        
        return list_string
    
    def pickRandom():
        lot = random.randint(1, 3)

        if lot == 1:
            return Reserve.pickSmall()
        elif lot == 2:
            return Reserve.pickMedium()
        else: return Reserve.pickLarge()

    def pickSmall():
        if not Reserve.small: return
        item = Reserve.small.pop()
        Reserve.total_volume -= item.volume
        return item

    def pickMedium():
        if not Reserve.medium: return
        item = Reserve.medium.pop()
        Reserve.total_volume -= item.volume
        return item

    def pickLarge():
        if not Reserve.large: return
        item = Reserve.large.pop()
        Reserve.total_volume -= item.volume
        return item