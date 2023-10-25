import copy, datetime
from v5.settings import *
from v5.reserve import *
from v5.sack import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()
        if not sack.add(item): break

    while True:
        item = reserve.pickSmallestVolume()
        if not sack.add(item): break

    return sack

def getNormalizedDistrs(distrs, coef, norms):
    normalized = []

    for i in range(len(distrs)):
        val_1 = distrs[i] * coef
        val_2 = norms[i] * ( 1 - coef )
        val_avg = ( val_1 + val_2 ) / 2

        normalized.append(val_avg)

    return normalized

def getAvgDistr(distrs):
    avgs = []

    for _ in range(len(distrs[0])):
        avgs.append(0)

    for distr in distrs:
        for i in range(len(distr)):
            avgs[i] += distr[i]

    for i in range(len(avgs)):
        avgs[i] /= len(distrs)

    return avgs


filename = datetime.datetime.now()
file = open(f'{S.path}/{filename}', 'w')
file.write(S.toString())
file.write(f'{S.data_start_str}\n')
file.close()


vol_normal = 1 / S.volume_category_count
vol_norms = []
for _ in range(S.volume_category_count):
    vol_norms.append(vol_normal)

counter = 0

for _ in range(S.total_iterations):
    sack_distrs = []
    sack_values = []
    reserve = Reserve()

    data_list = []

    for value in reserve.getVolumeDistribution():
        data_list.append(value)

    for value in reserve.getWeightDistribution():
        data_list.append(value)

    for __ in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)
        if filled_sack.getTotalVolume() > res_copy.getTotalVolume():
            print('All reserve items fits in the sack, discarded...')
            continue
        sack_distrs.append(filled_sack.getVolumeDistribution())
        sack_values.append(filled_sack.getTotalValue())

    if not sack_distrs: continue
    

    min_value = min(sack_values)

    for i in range(len(sack_values)):
        sack_values[i] -= min_value

    max_value = max(sack_values)

    for i in range(len(sack_values)):
        sack_values[i] /= max_value

    for i in range(len(sack_distrs)):
        sack_distrs[i] = getNormalizedDistrs(sack_distrs[i], sack_values[i], vol_norms)

    avg_distr = getAvgDistr(sack_distrs)
    

    for value in avg_distr:
        data_list.append(value)

    data_str = str(data_list)
    data_str = data_str[1:-1]
    data_str = data_str.replace(' ', '')

    file = open(f'{S.path}/{filename}', 'a')
    file.write(f'{data_str}\n')
    file.close()

    print(f'{counter}: {str(data_list)}')

    counter += 1