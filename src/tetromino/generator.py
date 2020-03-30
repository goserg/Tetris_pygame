from random import randrange
from tetromino.collection import *
import level


def get_new():
    n = randrange(7)
    if n == 0:
        t = TypeI()
    elif n == 1:
        t = TypeJ()
    elif n == 2:
        t = TypeL()
    elif n == 3:
        t = TypeO()
    elif n == 4:
        t = TypeS()
    elif n == 5:
        t = TypeT()
    else:
        t = TypeZ()
    for i in t.body:
        for j in level.cubes:
            if i.position == j.position:
                return None
    return t
