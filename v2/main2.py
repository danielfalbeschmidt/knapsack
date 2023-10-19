import copy
from item import *
from sack import *
from ml import *
from reserve import *

Ml.init_weights()

max_learn_iter = 10000
reserve_item_count = 20

while reserve_item_count < 160:
    sack_volume = int(reserve_item_count / 10)
    max_sack_volume = int(reserve_item_count / 3)

    while sack_volume < max_sack_volume:
        pick_iterations = int(reserve_item_count / 10)

        saturation_point_averages = []
        saturated_weights = []

        for _ in range(max_learn_iter):
            weights_before = Ml.getWeights()

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


            weights_after = Ml.getWeights()

            if round(weights_before[0], 4) == round(weights_after[0], 4) \
                and round(weights_before[1], 4) == round(weights_after[1], 4):
                saturated_weights.append(weights_after)
                Ml.init_weights()
            
            if len(saturated_weights) >= 100: break


        l = len(saturated_weights)
        s1 = 0
        s2 = 0
        s3 = 0

        for w in saturated_weights:
            s1 += w[0]
            s2 += w[1]
            s3 += w[2]

        s1 /= l
        s2 /= l
        s3 /= l
        
        # f = open('./nn/data.md', 'a')
        # f.write( str(( reserve_item_count, sack_volume, s1, s2, s3 )) + '\n' )
        # f.close()

        print(f'Sack volume / reserve content max volume: {sack_volume} / {reserve_item_count}')
        print('Saturation point weight averages:')
        print(s1, s2, s3)

        sack_volume += 1

    reserve_item_count = int(reserve_item_count * 1.2)