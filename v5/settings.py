class S:
    # dont bother going under 4
    reserve_item_count = 100

    # too large sack and reserve is gonna have 
    # hard time bringing items large enough
    sack_volume = reserve_item_count * 0.2

    # the number of sacks per one reserve
    iterations_per_reserve = 100000

    total_iterations = 10
