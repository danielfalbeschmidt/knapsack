from v5.settings2 import *
from v5.item2 import *
import random

class Reserve:
    def __init__(self):
        self.item_count = S.reserve_item_count

        while True: # all reserve contents should not fit a sack
            self.item_categories = self.getItemCategories()
            if self.getTotalVolume() > S.sack_volume: break

    def getItemCategories(self):
        all_items = []
        
        for _ in range(S.volume_category_count):
            all_items.append([])

        for _ in range(S.reserve_item_count):
            item = Item()
            category_index = int(item.volume * S.volume_category_count)

            all_items[category_index].append(item)

        return all_items

    def getTotalVolume(self):
        total_volume = 0

        for category in self.item_categories:
            for item in category:
                total_volume += item.volume

        return total_volume
    
    def pickRandom(self):
        for _ in range(1000): # watchdog for bad luck
            category = self.item_categories[random.randint(0, S.volume_category_count - 1)]

            if not category: continue # maybe another category has items...

            return category.pop()
        
        print('Could not pick random item from reserve')

    def pickSmallestVolume(self):
        for i in range(len(self.item_categories)):
            category = self.item_categories[i]

            if not category: continue # maybe another category has items...

            volumes = []
            for item in category:
                volumes.append(item.volume)

            smallest_volume_index = volumes.index(min(volumes))
            smallest_volume_item = category[smallest_volume_index]

            del self.item_categories[i][smallest_volume_index]
            return smallest_volume_item

    def getVolumeDistribution(self):
        distr = []

        for i in range(S.volume_category_count):
            distr.append(len(self.item_categories[i]))

        for i in range(S.volume_category_count):
            distr[i] /= S.reserve_item_count

        return distr
    
    def getWeightDistribution(self):
        distr = []

        for _ in range(S.weight_category_count):
            distr.append(0)

        for category in self.item_categories:
            for item in category:
                distr[item.weight_category] += 1

        for i in range(S.weight_category_count):
            distr[i] /= S.reserve_item_count

        return distr
