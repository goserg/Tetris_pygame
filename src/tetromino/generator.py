from random import randrange
from tetromino.collection import *
import level
import shade


def get_new():
    n = randrange(7)
    if n == 0:
        t = TypeI()
        shade.shade = TypeI()
    elif n == 1:
        t = TypeJ()
        shade.shade = TypeJ()
    elif n == 2:
        t = TypeL()
        shade.shade = TypeL()
    elif n == 3:
        t = TypeO()
        shade.shade = TypeO()
    elif n == 4:
        t = TypeS()
        shade.shade = TypeS()
    elif n == 5:
        t = TypeT()
        shade.shade = TypeT()
    else:
        t = TypeZ()
        shade.shade = TypeZ()
    for i in t.body:
        for j in level.cubes:
            if i.position == j.position:
                return None
    return t
