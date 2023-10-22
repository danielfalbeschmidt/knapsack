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

def normalize(distrs, coef, norms):
    normalized = []

    for i in range(len(distrs)):
        val_1 = distrs[i] * coef
        val_2 = norms[i] * ( 1 - coef )
        val_avg = ( val_1 + val_2 ) / 2

        normalized.append(val_avg)

    return normalized


filename = datetime.datetime.now()
file = open(f'{S.path}/{filename}', 'w')
file.write(S.toString())
file.write(f'{S.data_start_str}\n')
file.close()


vol_normal = 1 / S.volume_category_count
vol_norms = []
for _ in range(S.volume_category_count):
    vol_norms.append(vol_normal)


for _ in range(S.total_iterations):
    sack_distrs = []
    sack_values = []
    reserve = Reserve()


    data_list = []

    for value in reserve.getVolumeDistribution():
        data_list.append(value)

    for value in reserve.getWeightDistribution():
        data_list.append(value)

    data_str = str(data_list)
    data_str = data_str[1:-1]
    data_str = data_str.replace(' ', '')

    file = open(f'{S.path}/{filename}', 'a')
    file.write(f'{data_str}\n')
    file.close()

    c = 0
    for __ in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        if filled_sack.getTotalVolume() > res_copy.getTotalVolume():
            print('All reserve items fits in the sack, discarded...')
            continue

        sack_distrs.append(filled_sack.getVolumeDistribution())
        sack_values.append(filled_sack.getTotalValue())

        print('create',  str(c))
        c += 1

    if not sack_distrs: continue


    max_value = max(sack_values)

    c = 0
    for i in range(len(sack_values)):
        sack_values[i] /= max_value
        print('scale',  str(c))

    c = 0
    for i in range(len(sack_distrs)):
        sack_distrs[i] = normalize(sack_distrs[i], sack_values[i], vol_norms)
        print('normalize',  str(c))


    for sack_distr in sack_distrs:
        data_list = []

        for value in sack_distr:
            data_list.append(value)

        data_str = str(data_list)
        data_str = data_str[1:-1]
        data_str = data_str.replace(' ', '')

        file = open(f'{S.path}/{filename}', 'a')
        file.write(f'{data_str}\n')
        file.close()
