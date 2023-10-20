import copy, datetime
from settings import *
from reserve import *
from sack import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()
        if not sack.add(item): return sack


filename = datetime.datetime.now()
file = open(f'./data/{filename}', 'w')
file.write(S.toString())
file.write('DATA START\n')
file.close()


for _ in range(S.total_iterations):
    sack_distrs = []
    sack_values = []
    reserve = Reserve()

    for __ in range(S.iterations_per_reserve):
        res_copy = copy.deepcopy(reserve)
        filled_sack = getFilledSack(res_copy)

        if filled_sack.getTotalVolume() > res_copy.getTotalVolume():
            print('All reserve items fits in the sack, discarded...')
            continue

        sack_distrs.append(filled_sack.getVolumeDistribution())
        sack_values.append(filled_sack.getTotalValue())

    if not sack_distrs: continue

    best_sack_index = sack_values.index(max(sack_values))
    best_sack_distr = sack_distrs[best_sack_index]


    data_str = str( (
        (
            reserve.getVolumeDistribution(),
            reserve.getWeightDistribution()
        ),
        best_sack_distr
        ) )

    file = open(f'./data/{filename}', 'a')
    file.write(f'{data_str}\n')
    file.close()


file = open(f'./data/{filename}', 'a')
file.write('DATA END\n')
file.close()
