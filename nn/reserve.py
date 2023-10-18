from item import *

class Reserve:
    def __init__(self, count=0):
        self.small = []
        self.medium = []
        self.large = []

        self.count = count
        items = self.populate()
        self.total_volume = self.getTotalVolume(items)        
        sorted_items = self.sortByVolume(items)
        self.categorize(sorted_items)

    def populate(self):
        items = []

        for _ in range(self.count):
            items.append(Item())

        return items
    
    def sortByVolume(self, items):
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

    def categorize(self, items):
        for item in items:
            if item.volume_category == Measure.SMALL:
                self.small.append(item)
            elif item.volume_category == Measure.MEDIUM:
                self.medium.append(item)
            else: self.large.append(item)

    def getTotalVolume(self, items):
        total = 0

        for item in items:
            total += item.volume

        return total

    def printDetails(self):
        print('*** RESERVE ***')
        print(f'Total volume: {round(self.total_volume, 3)}')
        print('Item volumes by categories:')
        print(f'  Small:  {self.itemsToString(self.small)}')
        print(f'  Medium: {self.itemsToString(self.medium)}')
        print(f'  Large:  {self.itemsToString(self.large)}\n')

    def itemsToString(self, list):
        list_string = ''

        for item in list:
            list_string += f' {round(item.volume, 3)}'
        
        return list_string
    
    def pickRandom(self):
        item = None

        while not item:
            lot = random.randint(1, 3)
            
            if lot == 1: item = self.pickSmall()
            elif lot == 2: item = self.pickMedium()
            else: item = self.pickLarge()

        return item

    def pickSmall(self):
        if not self.small: return
        item = self.small.pop(random.randint(0, len(self.small) - 1))
        self.total_volume -= item.volume
        return item

    def pickMedium(self):
        if not self.medium: return
        item = self.medium.pop(random.randint(0, len(self.medium) - 1))
        self.total_volume -= item.volume
        return item

    def pickLarge(self):
        if not self.large: return
        item = self.large.pop(random.randint(0, len(self.large) - 1))
        self.total_volume -= item.volume
        return item

    def getDistributions(self):
        s_sum = len(self.small) + len(self.medium) + len(self.large)
        s1 = len(self.small) / s_sum
        s2 = len(self.medium) / s_sum
        s3 = len(self.large) / s_sum

        # volumes, weights: SMALL, MEDIUM, LARGE
        distributions = [s1, s2, s3, 0, 0, 0]

        all_items = self.small + self.medium + self.large

        for item in all_items:
            if item.weight_category == Measure.SMALL:
                distributions[3] += 1
            elif item.weight_category == Measure.MEDIUM:
                distributions[4] += 1
            else: distributions[5] += 1

        for i in range(3, 6):
            distributions[i] /= len(all_items)

        return distributions