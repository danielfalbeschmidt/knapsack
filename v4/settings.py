class S:
    reserve_item_count = 60 # affects data creation computation time

    # heuristical, too small value -> all items fit (no point in KP)
    sack_volume = int( reserve_item_count / 6 )

    # category_count <= sack_volume
    volume_category_count = 3
    weight_category_count = 3

    iterations_per_reserve = 1000 # one is the winner of this number of sacks per reserve
    total_iterations = 100000 # training sample count

    data_description = 'reserve_volume_distr,reserve_weight_distr,winner_sack_volume_distr'

    path = './data'
    # path = './v4/data'
    datafile = f'{path}/2023-10-23 08:19:16.452743'
    modelfile = f'{path}/model.json'
    weightsfile = f'{path}/model_weights.h5'
    data_start_str = 'DATA START'

    hidden_layer_count = 6
    train_ratio = 0.9
    epoch_count = 20

    def toString():
        return \
            f'volume_category_count: {S.volume_category_count}\n'\
            f'weight_category_count: {S.weight_category_count}\n'\
            f'reserve_item_count: {S.reserve_item_count}\n'\
            f'sack_volume: {S.sack_volume}\n'\
            f'iterations_per_reserve: {S.iterations_per_reserve}\n'\
            f'data description: {S.data_description}\n'
            