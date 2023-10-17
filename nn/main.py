import copy
from item import *
from sack import *
from ml import *
from reserve import *

total_iterations = 1000
reserve_item_count = 100

pick_iterations = int(reserve_item_count / 10)

saturated_weights = []

volume_distrs = []
success_rates = []

Ml.init_weights()

for _ in range(total_iterations):
    weights_before = Ml.getWeights()

    reserve = Reserve(reserve_item_count)

    for ___ in range(pick_iterations):
        current_reserve = copy.deepcopy(reserve)
        sack = Sack(reserve_item_count / 10)

        while True:
            if not sack.add(current_reserve.pickRandom()): break

        volume = sack.getTotalVolume()
        weight = sack.getTotalWeight()

        volume_distrs.append(sack.getVolumeDistribution())
        success_rates.append( weight / volume )

        winner_index = success_rates.index(max(success_rates))
        Ml.feed(volume_distrs[winner_index], success_rates[winner_index])

    Ml.printDetails()

    weights_after = Ml.getWeights()

    for i in range(3):
        if round(weights_before[i], 4) == round(weights_after[i], 4):
            saturated_weights.append(weights_after)
            print('Saturated, re-init weights...')
            Ml.init_weights()
            break

l = len(saturated_weights)
s1 = 0
s2 = 0
s3 = 0

for w in saturated_weights:
    s1 += w[0]
    s2 += w[1]
    s3 += w[2]

s1 /= l
s2 /= l
s3 /= l

print('Saturation point weight averages:')
print(s1, s2, s3)