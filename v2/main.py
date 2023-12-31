import copy
from item import *
from sack import *
from ml import *
from reserve import *

Ml.init_weights()

max_learn_iter = 1
reserve_item_count = 100

sack_volume = int(reserve_item_count / 10)
pick_iterations = 10

for _ in range(max_learn_iter):
    volume_distrs = []
    success_rates = []

    reserve = Reserve(reserve_item_count)

    if reserve.total_volume <= sack_volume: continue

    for ___ in range(pick_iterations):
        current_reserve = copy.deepcopy(reserve)
        sack = Sack(sack_volume)

        while True:
            picked_item = current_reserve.pickRandom()

            if not picked_item: continue
            if not sack.add(picked_item): break
            

        volume = sack.getTotalVolume()
        weight = sack.getTotalWeight()

        volume_distrs.append(sack.getVolumeDistribution())
        success_rates.append( weight / volume )


    best_success_rate = max(success_rates)
    best_rate_index = success_rates.index(best_success_rate)

    for i in range(len(success_rates)):
        success_rates[i] /= best_success_rate


    Ml.feed(volume_distrs[best_rate_index], success_rates[best_rate_index])

    Ml.printDetails()


l1 = 0
l2 = 0

for _ in range(1000):

    reserve = Reserve(reserve_item_count)


    sack_1 = Sack(sack_volume)

    while True:
        picked_item = reserve.pickRandom()

        if not picked_item: continue
        if not sack_1.add(picked_item): break


    sack_2 = Sack(sack_volume)

    while True:
        picked_item = reserve.pickWithDistr((0.98, 0.01, 0.01))

        if not picked_item: continue
        if not sack_2.add(picked_item): break

    print(sack_2.getVolumeDistribution())

    l1 += sack_1.getTotalValue()
    l2 += sack_2.getTotalValue()

print(l1, l2)


