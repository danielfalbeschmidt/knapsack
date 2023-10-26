import copy, datetime
from settings import *
from reserve import *
from sack import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()

        if not sack.add(item):
            reserve.returnItem(item)
            break

    while True:
        item = reserve.pickBestRemaining(sack.space)
        if not item: break

        if not sack.add(item):
            reserve.returnItem(item)
            break

    return sack


reserve = Reserve()
reserve.printDetails()

print(f'Sack capacity: {S.sack_volume}')

for __ in range(S.total_iterations):
    picked_items = []
    sack_values = []
    value_set = { 0.0 }
    best_pick = None

    for i in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        sack_value = filled_sack.getTotalValue()
        
        if sack_value in value_set:
            i -= 1
            continue

        value_set.add(sack_value)

        if sack_value == max(value_set):
            best_pick = copy.deepcopy(res_copy.picked)

        picked_items.append(res_copy.picked)
        sack_values.append(sack_value)


    max_value = max(sack_values)
    
    if not max_value:
        print('No items picked, retrying...')
        continue

    min_value = min(sack_values)

    r = range(len(sack_values))
    c = range(S.reserve_item_count)

    for i in r: sack_values[i] -= min_value

    for i in r: sack_values[i] /= max_value

    for i in r:
        for j in c: picked_items[i][j] *= sack_values[i]

    
    cumul_picks = [ 0 for _ in range(S.reserve_item_count) ]

    for i in r:
        for j in c: cumul_picks[j] += picked_items[i][j]


    min_cumul = min(cumul_picks)
    for i in c: cumul_picks[i] -= min_cumul

    max_cumul = max(cumul_picks)
    for i in c: cumul_picks[i] /= max_cumul


    vol_sum = reserve.getItemVolumeSum(cumul_picks)

    while vol_sum < S.sack_volume:
        unused_inds = []
        unused_vals = []

        for i in range(S.reserve_item_count):
            if not round(cumul_picks[i]):
                unused_inds.append(i)
                unused_vals.append(cumul_picks[i])

        unused_max_ind = unused_inds[unused_vals.index(max(unused_vals))]
        cumul_picks[unused_max_ind] = 1

        vol_sum = reserve.getItemVolumeSum(cumul_picks)

    while vol_sum > S.sack_volume:
        used_inds = []
        used_vals = []

        for i in range(S.reserve_item_count):
            if round(cumul_picks[i]):
                used_inds.append(i)
                used_vals.append(cumul_picks[i])

        used_max_ind = used_inds[used_vals.index(min(used_vals))]
        cumul_picks[used_max_ind] = 0

        vol_sum = reserve.getItemVolumeSum(cumul_picks)


    for i in c: cumul_picks[i] = round(cumul_picks[i])


    print(f'Volume: {round(reserve.getItemVolumeSum(cumul_picks), 3)}', end='\t')
    print(f'Weight: {round(reserve.getItemWeightSum(cumul_picks), 3)}', end='\t')
    print(f'Value: {round(reserve.getItemValueSum(cumul_picks), 3)}', end='\t')
    print(f'Weight / Volume: {round(reserve.getWeightToVolumeSum(cumul_picks), 3)}', end='\t\t')
    print(f'Picked items: ', end='\t')
    for pick in cumul_picks:
        print(pick, end='')
    print('')


    print(f'Volume: {round(reserve.getItemVolumeSum(best_pick), 3)}', end='\t')
    print(f'Weight: {round(reserve.getItemWeightSum(best_pick), 3)}', end='\t')
    print(f'Value: {round(reserve.getItemValueSum(best_pick), 3)}', end='\t')
    print(f'Weight / Volume: {round(reserve.getWeightToVolumeSum(best_pick), 3)}', end='\t\t')
    print(f'Picked items: ', end='\t')
    for pick in best_pick:
        print(pick, end='')
    print('')
    print('')
