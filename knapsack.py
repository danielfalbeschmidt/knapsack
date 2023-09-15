import random
from heapalgorithm import HeapAlgorithm

class K:

   max_item_size = 10000 # big values for big randomness
   max_item_weight = 10000 # remarkably enough, size and weight appear to not have significant effect on favorable permutations
   # item_count = 3 # use wisely, permutation count becomes the factorial of item_count
   item_count = 3 # !!! for now, only item_count of 3 is supported
   weights = [1, 2, 3] # item "goodness" values, i.e. greater is better (pure gold!)
   sizes = [3, 4, 5] # item sizes in relation to sack_vol
   sack_vol = 11 # must be less than the sum of items
   item_orders = [] # values for indexing K.sizes
   perm_inds = [] # indices of permutations used in item_orders
   permutations = []


   def setPermutations():
      K.permutations = HeapAlgorithm.getPermutations(K.item_count)


   def setItemCount(n):
      K.item_count = n


   def init():
      K.weights = []
      K.sizes = []
      K.perm_inds = []

      for _ in range(K.item_count):
         K.sizes.append(random.randint(1, K.max_item_size))
         K.weights.append(random.randint(1, K.max_item_weight))

      K.sack_vol = random.randint(min(K.sizes), sum(K.sizes))
      K.sizes = sorted(K.sizes)
      K.item_orders = K.getItemOrders()


   def printSpecs():
      print(f'Weights: {K.weights}')
      print(f'Sizes: {K.sizes}')
      print(f'Sack Volume: {K.sack_vol}')
      print(f'Permutations used, indices: {K.perm_inds}')


   def getItemOrders(): # filter overlapping permutations
      item_orders = [] # unique list of item index lists that fit the sack

      item_orders.append(K.getLimitedItems(K.permutations[0]))
      K.perm_inds.append(0)

      i = 0
      for p in K.permutations[1:]:
         i += 1

         # get as many items of this p that can fit the sack
         new_item_order = K.getLimitedItems(p)

         # eliminate duplicate sets of items
         order_exist = K.orderExist(item_orders, new_item_order)
         if not order_exist and new_item_order:
            item_orders.append(new_item_order)
            K.perm_inds.append(i)

      return item_orders
   

   def getLimitedItems(item_permutation):
      item_order = [] # one index list, referenced items fit the sack
      item_sum = 0 # cumulative sum, compared to sack_vol

      for index in item_permutation:
         items = K.sizes[index]
         if item_sum + items > K.sack_vol: break
         item_order.append(index)
         item_sum += items

      return sorted(item_order)
   

   def orderExist(item_orders, compare_order):
      for items in item_orders:
         if set(items) == set(compare_order): return True
      return False
   

   def fillSack(item_order):
      product_sum = 0 # sizes * weights
      sack_state = 0 # occupied volume

      # fill the sack, all items are expected to fit (calculated elsewhere)
      for index in item_order:
         item_size = K.sizes[index]
         sack_state += item_size
         product_sum += item_size * K.weights[index]

      spare_space = K.sack_vol - sack_state

      # goal: minimize spare_space and maximize product_sum
      return product_sum - spare_space
   
   def getBestPermutations(index_list):
      best_perms = []

      for i in index_list:
         best_perms.append(K.permutations[i])

      return best_perms


   


