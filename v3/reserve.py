from settings import *
from item import *
import random

class Reserve:
    def __init__(self):
        self.item_count = Settings.reserve_item_count
        self.items = self.populate()

    def populate(self):
        all_items = []

        for _ in range(Settings.volume_category_count):
            all_items.append([])

        for _ in range(Settings.reserve_item_count):
            item = Item()
            category_index = int(item.volume * 10)

            all_items[category_index].append(item)

        return all_items
    
    def pickRandom(self):
        category = self.items[random.randint(0, Settings.volume_category_count - 1)]

        if not category: return
        return category[random.randint(0, len(category) - 1)]
