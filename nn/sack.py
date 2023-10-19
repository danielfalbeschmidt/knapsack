from item import *

class Sack:
    def __init__(self, volume=0):
        self.items = [] # sack contents, item objs + empty space
        self.volume = volume # sack total item volume capacity
        self.space = self.volume # empty space left in the sack

    def add(self, item):
        if item.volume > self.space: return
        
        self.space -= item.volume
        self.items.append(item)
        return True

    def getTotalWeight(self):
        total = 0

        for item in self.items:
            total += item.weight

        return total

    def getTotalVolume(self):
        total = 0

        for item in self.items:
            total += item.volume

        return total

    def getTotalValue(self):
        total = 0

        for item in self.items:
            total += item.value

        return total
    
    def sortItems(self):
        sorted_items = []
        moved_item = self.items.pop()
        sorted_items.append(moved_item)

        while self.items:
            moved_item = self.items.pop()

            for index in range(len(sorted_items)):
                if moved_item.volume_category < sorted_items[index].volume_category:

                    sorted_items.insert(index, moved_item)
                    break
                
                if moved_item.volume_category == sorted_items[index].volume_category and \
                    moved_item.weight < sorted_items[index].weight:

                    sorted_items.insert(index, moved_item)
                    break

            else: sorted_items.insert(len(sorted_items), moved_item)

        self.items = sorted_items

    def getVolumeDistribution(self):
        # SMALL, MEDIUM, LARGE
        distributions = [0, 0, 0]

        for item in self.items:
            if item.volume_category == Measure.SMALL:
                distributions[0] += 1
            elif item.volume_category == Measure.MEDIUM:
                distributions[1] += 1
            else: distributions[2] += 1

        for i in range(3):
            distributions[i] /= len(self.items)

        return distributions
    
    def printDetails(self):
        print('*** SACK ***')
        print(f'Total volume: {round(self.volume, 3)}')
        print(f'Space left: {round(self.space, 3)}')
        print(f'Space occupied: {round(self.volume - self.space, 3)}')
        print(f'Items total value: {round(self.getTotalValue(), 3)}')
        print(f'Distributions [volumes 3, weights 3]: {self.getVolumeDistribution()}')
        # print(f'Item category values: {self.itemsToString()}\n')

    def itemsToString(self):
        list_string = ''

        for item in self.items:
            list_string += f'\n  {item.toString()}'
        
        if not list_string: return ' No items'
        return list_string
