import matplotlib.pyplot as plt, math
from knapsack import K

iterations = 100
K.setItemCount(6)
perm_range = range(math.factorial(K.item_count))

r = [] # permutation scores
for _ in perm_range:
    r.append(0)

for _ in range(iterations):
    K.init()
    # K.printSpecs()

    for i in range(len(K.item_orders)):
        perm_index = K.perm_inds[i]
        item_order = K.item_orders[i]
        
        sack_state = K.fillSack(item_order)
        
        r[perm_index] += sack_state


m = max(r)

for i in perm_range:
    r[i] = round( r[i] / m, 2 )

bar_arr = []
for i in perm_range:
    bar_arr.append(i)

plt.bar(bar_arr, r)
 
plt.xlabel('Permutation no.')
plt.ylabel('Performance (perm. points = size * weight - waste_space)\n')
plt.title(f'{K.item_count} item knapsack problem, trial count {iterations}.\n'\
            'Items are ordered by size (asc). Randomized values:\n'\
            'sizes, weigths, sack_vol (with limitations). For\n'\
            'each indexing permutation, items are added from left\n'\
            'to right until no room for next.')
plt.show()


