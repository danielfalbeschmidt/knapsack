import copy
from reserve import *
from sack import *

def getFilledSack(reserve, sack_volume):
    sack = Sack(sack_volume)

    while True:
        item = reserve.pickRandom()

        if not sack.add(item): # item didn't fit
            reserve.returnToReserve(item)

            # at least one item should be in the returned sack
            if sack.items: break

    # no point in further search if even the smallest reserve item wouldn't fit
    if reserve.smallest_item_vol > sack.space: return sack
    
    while True:
        # pick the most valuable fit item
        item = reserve.pickBestRemaining(sack.space)

        if not item: break # no fit items left

        if not sack.add(item): # item didn't fit
            reserve.returnToReserve(item)

    return sack

def moreItems(pick_profile, item_count):
    unused_inds = []
    unused_vals = []

    for i in range(item_count):
        # if profile value would be interpreted as 0,
        # it is noted as unused
        if not round(pick_profile[i]):
            unused_inds.append(i)
            unused_vals.append(pick_profile[i])

    # amongst unused picks, the maximum is selected and its 
    # index used to access the respective profile value
    unused_max_ind = unused_inds[unused_vals.index(max(unused_vals))]
    # it's ok to toggle it to 1 now, pick_profile value comparison
    # for toggled-to-1 values is binary for now on anyway
    pick_profile[unused_max_ind] = 1

def lessItems(pick_profile, item_count):
    used_inds = []
    used_vals = []

    for i in range(item_count):
    # if profile value would be interpreted as 1,
    # it is noted as already in use
        if round(pick_profile[i]):
            used_inds.append(i)
            used_vals.append(pick_profile[i])

    # amongst already used picks, the minimum is selected and 
    # its index used to access the respective profile value
    used_max_ind = used_inds[used_vals.index(min(used_vals))]
    # it's ok to toggle it to 0 now, pick_profile value comparison
    # for toggled-to-0 values is binary for now on anyway
    pick_profile[used_max_ind] = 0

def printPickProfile(pick_profile):
    print(f'Volume: {round(reserve.getItemVolumeSum(pick_profile), 3)}', end='\t')
    print(f'Weight: {round(reserve.getItemWeightSum(pick_profile), 3)}', end='\t')
    print(f'Value: {round(reserve.getItemValueSum(pick_profile), 3)}', end='\t')
    # print(f'Weight / Volume: {round(reserve.getWeightToVolumeSum(pick_profile), 3)}', end='\t\t')
    print(f'Picked items: ', end='\t')
    for pick in pick_profile:
        print(pick, end='')
    print('')


res_size_rounds = []

# test on reserves of different sizes
for res_size_round in range( 9, 11 ):
    reserve_item_count = res_size_round * 10
    sack_volume = reserve_item_count * 0.2
    # original reserve, this is later being copied
    reserve = Reserve( reserve_item_count )
    sample_count_rounds = []

    print(f'Reserve item count: {reserve_item_count}')
    print(f'Sack volume: {sack_volume}')
    
    # test with different number of samples per each size of reserve
    for sample_count_round in range( 1, 1001 ):
        all_picks = [] # [ [ 0, 1, ... ], ... ]
        all_values = [] # [ 3.45, 4.56, ... ]
        value_set = { 0.0 } # for duplicate monitoring
        best_pick = None # [ 0, 1, ... ] later compared to pick_profile
        sample_count = sample_count_round * 100

        # test with different random item picks
        for i in range( sample_count ):
            res_copy = copy.deepcopy(reserve)
            filled_sack = getFilledSack( res_copy, sack_volume )

            # items total volume * weight
            sack_value = filled_sack.getTotalValue()
            
            # if identical sack already exists, don't count it in
            if sack_value in value_set:
                i -= 1
                continue

            value_set.add(sack_value)

            # if this value is highest yet, relate that 
            # new top score to corresponding pick profile
            if sack_value == max(value_set):
                best_pick = copy.deepcopy(res_copy.picked)

            all_picks.append(res_copy.picked)
            all_values.append(sack_value)


        r = range(len(all_values))
        c = range(reserve_item_count)
        
        
        # min value becomes 0
        min_value = min(all_values)
        for i in r: all_values[i] -= min_value

        # values scaled to range 0-1
        max_value = max(all_values)
        for i in r: all_values[i] /= max_value

        # each representation of selected reserve items is 
        # multiplied by the value its corresponding sack yielded
        for i in r:
            for j in c: all_picks[i][j] *= all_values[i]

        
        # each value in this list holds the sum of all the
        # weighted values in corresponding indices of all_picks
        pick_profile = [ 0 for _ in c ]
        for i in r:
            for j in c: pick_profile[j] += all_picks[i][j]

        # min value becomes 0
        min_cumul = min(pick_profile)
        for i in c: pick_profile[i] -= min_cumul

        # values scaled to range 0-1
        max_cumul = max(pick_profile)
        for i in c: pick_profile[i] /= max_cumul


        # too modest: toggle to 1 more next most favorable items to pick_profile
        while reserve.getItemVolumeSum(pick_profile) < sack_volume:
            moreItems( pick_profile, reserve_item_count )

        # too greedy: toggle to 0 more next most unfavorable items to pick_profile
        while reserve.getItemVolumeSum(pick_profile) > sack_volume:
            lessItems( pick_profile, reserve_item_count )

        # pick_profile values are made binary by rounding
        for i in c: pick_profile[i] = round(pick_profile[i])


        print(f'Samples: {sample_count},', \
              f'Values - ' \
              f'Avgs: {round(reserve.getItemValueSum(pick_profile), 3)}, ' \
              f'Best: {round(reserve.getItemValueSum(best_pick), 3)}')

        sample_count_rounds.append(pick_profile)

    res_size_rounds.append(sample_count_rounds)


