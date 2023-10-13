from item import *
from sack import *
from reserve import *

Reserve.create(27)
Sack.setVolume(4)

Reserve.printDetails()
Sack.printDetails()

while True:
    random_item = Reserve.pickRandom()
    if not random_item: continue
    if not Sack.add(random_item): break

print('\nSack filled\n')

Reserve.printDetails()
Sack.printDetails()
