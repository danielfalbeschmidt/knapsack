import matplotlib.pyplot as plt
from knapsack import K

r = [0, 0, 0, 0, 0, 0]
iterations = 1000

for _ in range(iterations):
    K.init(3)
    # K.printSpecs()

    for i in range(len(K.item_orders)):
        perm_index = K.perm_inds[i]
        item_order = K.item_orders[i]
        
        sack_state = K.fillSack(item_order)
        
        r[perm_index] += sack_state


m = max(r)

for i in range(len(r)):
    r[i] = round( r[i] / m, 2 )

print(r)

plt.bar([0,1,2,3,4,5], r)
 
plt.xlabel('Permutation no.')
plt.ylabel('Performance (perm. points = size * weight - waste_space)\n')
plt.title(f'Three item knapsack problem, trial count {iterations}.\n'\
            'Items are ordered by size (asc). Randomized values:\n'\
            'sizes, weigths, sack_vol (with limitations). For\n'\
            'each indexing permutation, items are added from left\n'\
            'to right until no room for next.')
plt.show()


