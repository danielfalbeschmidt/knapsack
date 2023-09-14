import math, random

sack_volume = 0.9

i1 = 0.1 # sack item volumes
i2 = 0.2
i3 = 0.3
i4 = 0.4

weights = [] # get random weights btw 0-1
for _ in range(3):
    weights.append(random.random())
last_weight_ind = len(weights - 1)


def learn(sack_items, spare_volume):
   error = sigmoid(spare_volume)

   for i in range(len(sack_items)):
      weights[i] = error * sack_items[i]

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def get_spare_volume(sack_items):
   item_sum = 0.0

   for item in sack_items:
      item_sum += item

   return sack_volume - item_sum


new_volume = 2.4
a = 0.6
b = 0.7
c = 0.8
d = 0.9

inds = set()

for _ in range(1000):
   for i in range(100):
      learn([i1, i2, i3], get_spare_volume([i1, i2, i3]))
      learn([i1, i2, i4], get_spare_volume([i1, i2, i4]))
      learn([i2, i3, i4], get_spare_volume([i2, i3, i4]))

   o1 = a * weights[0] + b * weights[1] + c * weights[2] + new_volume * weights[3]
   o2 = a * weights[0] + b * weights[1] + d * weights[2] + new_volume * weights[3]
   o3 = a * weights[0] + c * weights[1] + d * weights[2] + new_volume * weights[3]
   o4 = b * weights[0] + c * weights[1] + d * weights[2] + new_volume * weights[3]

   all = [o1, o2, o3, o4]
   inds.add(all.index(max(all)))

print(inds)