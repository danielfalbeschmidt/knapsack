class S:
    reserve_item_count = 60 # affects data creation computation time

    # heuristical, too small value -> all items fit (no point in KP)
    sack_volume = reserve_item_count / 4

    iterations_per_reserve = 100000 # the number of sacks per one reserve
    total_iterations = 10000 # training sample count
