from item import *
from size import *
from sack import *
from ml import *
from reserve import *

Sack.setVolume(9)
Reserve.create(81)

for _ in range(10000):
    while True:
        random_item = Reserve.pickRandom()
        if not random_item: continue
        if not Sack.add(random_item): break

    Ml.learn()

    Reserve.reset()
    Reserve.create(81)
    Sack.empty()

Ml.printDetails()
