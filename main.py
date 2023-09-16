import matplotlib.pyplot as plt, math
from knapsack import K

start_perms = 3 # item count at the beginning
stop_perms = 10 # end (not included)

# partially determines the score collecting iteration count:
hardness = math.factorial(stop_perms)

for n in range(start_perms, stop_perms):
    item_count = n # how many items are permutated
    count_fact = math.factorial(item_count)
    perm_range = range(count_fact)

    K.setItemCount(item_count)
    K.setPermutations()

    scores = [] # score tracking per each permutation
    for _ in perm_range:
        scores.append(0)

    iterations = int(hardness / count_fact) # number of score counting trials
    for _ in range(iterations):
        K.init()

        for i in range(len(K.item_orders)):
            perm_index = K.perm_inds[i]
            item_order = K.item_orders[i]
            
            sack_state = K.fillSack(item_order)
            
            scores[perm_index] += sack_state





    score_map = {} # score : index
    max_score = max(scores)
    score_lim = max_score / 10
    for i in perm_range:
        score = scores[i]
        if score < score_lim: continue
        score_map[score] = i

    sorted_scores = sorted(scores)
    sorted_scores.reverse()

    top_perm_inds = []

    for score in sorted_scores:
        if score not in score_map: continue
        top_perm_inds.append(score_map[score])
    
    top_perms = []
    for i in top_perm_inds:
        top_perms.append(K.permutations[i])

    for i in top_perm_inds:
        print(K.permutations[i])

    print('')
    





    # index_ratios = []
    # perms = []
    # max_score = max(scores)
    # half_max_score = max_score / 2

    # for i in perm_range:
    #     score = scores[i]
    #     if score < half_max_score: continue
    #     index_ratios.append(i / count_fact)
    #     perms.append(K.permutations[i])

    # print(perms)





    # bar_arr = []
    # for i in perm_range:
    #     bar_arr.append(i)

    # plt.bar(bar_arr, scores)
    
    # plt.show()



