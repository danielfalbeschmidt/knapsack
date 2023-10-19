from reserve import *
from sack import *

def getFilledSack(reserve):
    sack = Sack()

    while True:
        item = reserve.pickRandom()

        if not item: continue
        if not sack.add(item): return sack

reserve = Reserve()
