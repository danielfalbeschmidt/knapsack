import math, random

class K:

   items = [3, 4, 5]
   sack_vol = 11 # must be less than the sum of items

   def getItemOrders(): # filter overlapping permutations
      item_orders = [] # unique list of item index lists that fit the sack

      permutations = K.getPermutations()
      for p in permutations:
         item_order = [] # one index list, referenced items fit the sack
         item_sum = 0 # cumulative sum, compared to sack_vol
         
         for index in p:
            items = K.items[index]
            if item_sum + items > K.sack_vol: break
            item_order.append(index)
            item_sum += items

         order_exist = False
         for items in item_orders:
            if set(items) == set(item_order):
               order_exist = True
               break
         if not order_exist and item_order:
            item_orders.append(sorted(item_order))

         if not item_orders and item_order:
            item_orders.append(sorted(item_order))

      return item_orders

   def getPermutations():
      # heap's algorithm would be great
      # HeapAlgorithm.getPermutations( len(self.items) - 1 )
      return [
           [0, 1, 2]
         , [0, 2, 1]
         , [1, 0, 2]
         , [1, 2, 0]
         , [2, 0, 1]
         , [2, 1, 0]
      ]
   
   def fillSack(item_order):
      sack_state = 0

      # fill the sack, spare space should be guaranteed
      for index in item_order:
         sack_state += K.items[index]

      # return leftover space in sack
      return K.sack_vol - sack_state
   


