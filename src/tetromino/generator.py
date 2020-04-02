from random import randrange
from tetromino.collection import *


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
    return t
