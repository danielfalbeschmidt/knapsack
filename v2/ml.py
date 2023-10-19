import random, math
from sack import *

class Ml:
    learning_rate = 100 # bigger for less sensitivity

    w_small = 1 / 3
    w_medium = 1 / 3
    w_large = 1 / 3

    def init_weights(): # sum of weights = 1
        Ml.w_small = random.random()
        Ml.w_medium = random.random()
        Ml.w_large = random.random()

        scale = 1 / ( Ml.w_small + Ml.w_medium + Ml.w_large )

        Ml.w_small *= scale
        Ml.w_medium *= scale
        Ml.w_large *= scale

    def feed(volume_dist, success_rate):
        if 0 in volume_dist or success_rate < 1: return
        
        success_rate /= Ml.learning_rate

        # previous weights, inversely proportional to success_rate
        p_w_small = Ml.w_small * ( 1 - success_rate )
        p_w_medium = Ml.w_medium * ( 1 - success_rate )
        p_w_large = Ml.w_large * ( 1 - success_rate )

        # learn values, proportional to success_rate
        l_small = volume_dist[0] * success_rate
        l_medium = volume_dist[1] * success_rate
        l_large = volume_dist[2] * success_rate

        Ml.w_small = p_w_small + l_small
        Ml.w_medium = p_w_medium + l_medium
        Ml.w_large = p_w_large + l_large

    def printDetails():
        print(f'{round(Ml.w_small, 4)}\t{round(Ml.w_medium, 4)}\t{round(Ml.w_large, 4)}')

    def getWeights():
        return (Ml.w_small, Ml.w_medium, Ml.w_large)

