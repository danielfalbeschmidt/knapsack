class S:
    reserve_item_count = 100 # affects data creation computation time
    sack_volume = reserve_item_count * 0.2

    iterations_per_reserve = 100000 # the number of sacks per one reserve
    total_iterations = 10 # training sample count
