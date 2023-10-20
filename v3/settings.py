class S:
    volume_category_count = 6 # arbitrary
    weight_category_count = 6 # arbitrary

    reserve_item_count = 60 # affects data creation computation time
    sack_volume = reserve_item_count / 6 # heuristical, too small value -> all items fit (no point regarding KP)

    iterations_per_reserve = 1000 # arbitrary
    total_iterations = 100000 # arbitrary

    data_description = '(([ reserve_volume_distr ], [ reserve_weight_distr ]), [ winner_sack_volume_distr ])'

    def toString():
        return \
            f'volume_category_count: {S.volume_category_count}\n'\
            f'weight_category_count: {S.weight_category_count}\n'\
            f'reserve_item_count: {S.reserve_item_count}\n'\
            f'sack_volume: {S.sack_volume}\n'\
            f'iterations_per_reserve: {S.iterations_per_reserve}\n'\
            f'data description: {S.data_description}\n'
            