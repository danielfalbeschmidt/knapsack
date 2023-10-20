import copy
from settings import *
from reserve import *
from sack import *
from nn import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()
        if not sack.add(item): return sack


nn.initWeights()

reserve = Reserve()

reserve_distr = (
    reserve.getVolumeDistribution() +
    reserve.getWeightDistribution()
    )

for __ in range(S.iterations_per_reserve):
    res_copy = copy.deepcopy(reserve)
    filled_sack = getFilledSack(res_copy)

    sack_distr = filled_sack.getVolumeDistribution()
    sack_value = filled_sack.getTotalValue()

    nn.learn(reserve_distr, sack_distr, sack_value)
    nn.printOutputWeights()
