import copy, datetime
from settings import *
from reserve import *
from sack import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()
        if not sack.add(item): break

    while True:
        item = reserve.pickSmallestVolume()
        if not sack.add(item): break

    return sack


# filename = datetime.datetime.now()
# file = open(f'{S.path}/{filename}', 'w')
# file.write(S.toString())
# file.write(f'{S.data_start_str}\n')
# file.close()


avg_distr = [ random.random() for _ in range(S.reserve_item_count) ]
reserve = Reserve()

for _ in range(S.total_iterations):
    picked_items = []
    sack_values = []
    value_set = set()

    for __ in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        sack_value = filled_sack.getTotalValue()
        
        if sack_value in value_set: continue

        value_set.add(sack_value)
        picked_items.append(res_copy.picked)
        sack_values.append(sack_value)


    min_value = min(sack_values)
    for i in range(len(sack_values)):
        sack_values[i] -= min_value

    max_value = max(sack_values)
    for i in range(len(sack_values)):
        sack_values[i] /= max_value

    for i in range(len(picked_items)):
        for j in range(len(picked_items[i])):
            picked_items[i][j] *= sack_values[i]


    pick_distr = [ 0 for _ in range(S.reserve_item_count) ]

    for picks in picked_items:
        for i in range(len(pick_distr)):
            pick_distr[i] += picks[i]

    max_pick = max(pick_distr)
    for i in range(len(pick_distr)):
        pick_distr[i] /= max_pick


    for i in range(len(pick_distr)):
        avg_distr[i] = ( avg_distr[i] + pick_distr[i] ) / 2

    for p in avg_distr:
        print(round(p, 4), end='\t')

    print('')

    


    # data_str = str(data_list)
    # data_str = data_str[1:-1]
    # data_str = data_str.replace(' ', '')

    # file = open(f'{S.path}/{filename}', 'a')
    # file.write(f'{data_str}\n')
    # file.close()
