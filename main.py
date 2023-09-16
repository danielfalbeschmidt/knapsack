import matplotlib.pyplot as plt, math
from knapsack import K

iterations = 100 # number of score counting trials
item_count = 7 # how many items are permutated
count_fact = math.factorial(item_count)
perm_range = range(count_fact)

top_score_lim = 100 # number of tier 2 permutations
if count_fact < top_score_lim: top_score_lim = count_fact

K.setItemCount(item_count)
K.setPermutations()

scores = [] # score tracking per each permutation
for _ in perm_range:
    scores.append(0)

for _ in range(iterations):
    K.init()
    # K.printSpecs()

    for i in range(len(K.item_orders)):
        perm_index = K.perm_inds[i]
        item_order = K.item_orders[i]
        
        sack_state = K.fillSack(item_order)
        
        scores[perm_index] += sack_state

best_inds = set() # indices of top score permutations
for _ in range(top_score_lim):
    m = max(scores)
    i = scores.index(m)
    best_inds.add(i)
    scores[i] = 0 # zero after recording to get updated max on next iter

best_perms = K.getBestPermutations(best_inds)
K.permutations = best_perms
K.init()
r = range(len(best_perms))

scores = []
for i in r:
    scores.append(0)

for i in range(len(K.item_orders)):
    perm_index = K.perm_inds[i]
    item_order = K.item_orders[i]
    
    sack_state = K.fillSack(item_order)
    
    scores[perm_index] += sack_state

k = K.permutations[scores.index(max(scores))]
for x in k:
    print(f'ordinal: {x}, size: {K.sizes[x]}, weight: {K.weights[x]}')


# for i in perm_range:
#     r[i] = round( r[i] / m, 2 )

# bar_arr = []
# for i in perm_range:
#     bar_arr.append(i)

# plt.bar(bar_arr, r)
 
# plt.xlabel('Permutation no.')
# plt.ylabel('Performance (perm. points = size * weight - waste_space)\n')
# plt.title(f'{K.item_count} item knapsack problem, trial count {iterations}.\n'\
#             'Items are ordered by size (asc). Randomized values:\n'\
#             'sizes, weigths, sack_vol (with limitations). For\n'\
#             'each indexing permutation, items are added from left\n'\
#             'to right until no room for next.')
# plt.show()


