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


reserve = Reserve()

for __ in range(S.total_iterations):
    picked_items = []
    sack_values = []
    value_set = set()
    cumul_picks = [ 0 for _ in range(S.reserve_item_count) ]

    for _ in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        sack_value = filled_sack.getTotalValue()
        
        if sack_value in value_set: continue

        value_set.add(sack_value)
        picked_items.append(res_copy.picked)
        sack_values.append(sack_value)


    r = range(len(sack_values))
    c = range(S.reserve_item_count)

    min_value = min(sack_values)
    for i in r: sack_values[i] -= min_value

    max_value = max(sack_values)
    for i in r: sack_values[i] /= max_value

    for i in r:
        for j in c: picked_items[i][j] *= sack_values[i]

    for i in r:
        for j in c: cumul_picks[j] += picked_items[i][j]


    min_cumul = min(cumul_picks)
    for i in c: cumul_picks[i] -= min_cumul

    max_cumul = max(cumul_picks)
    for i in c: cumul_picks[i] /= max_cumul


    for p in cumul_picks:
        print(round(p), end='')
    print('')
    


    # data_str = str(data_list)
    # data_str = data_str[1:-1]
    # data_str = data_str.replace(' ', '')

    # file = open(f'{S.path}/{filename}', 'a')
    # file.write(f'{data_str}\n')
    # file.close()
