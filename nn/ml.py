import random, math
from sack import *
from size import *

class Ml:
    a1 = 0 # small
    a2 = 0 # medium
    a3 = 0 # large
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    success_rate = 0

    def printDetails():
        print('*** ML DETAILS ***')
        print(f'w1: {Ml.w1}')
        print(f'w2: {Ml.w2}')
        print(f'w3: {Ml.w3}')

    def learn():
        Ml.calculateDistribution()
        Ml.setSuccessRate()
        Ml.backPropagation()

    def calculateDistribution():
        small_count = 0
        medium_count = 0
        large_count = 0

        for item in Sack.items:
            category = Size.toString(item.category)

            if category == 'SMALL':
                small_count += 1
            elif category == 'MEDIUM':
                medium_count += 1
            else: large_count += 1

        total_count = len(Sack.items)

        Ml.a1 = small_count / total_count
        Ml.a2 = medium_count / total_count
        Ml.a3 = large_count / total_count

    def setSuccessRate():
        Ml.success_rate = Sack.getTotalValue()
    
    def backPropagation():
        Ml.w1 = Ml.sigmoid(Ml.a1 * Ml.success_rate)
        Ml.w2 = Ml.sigmoid(Ml.a2 * Ml.success_rate)
        Ml.w3 = Ml.sigmoid(Ml.a3 * Ml.success_rate)

    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
