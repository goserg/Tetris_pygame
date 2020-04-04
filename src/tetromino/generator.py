import random
from tetromino.collection import *

tetromino_set = (TypeI, TypeJ, TypeL, TypeO, TypeS, TypeT, TypeZ)


def get_new():
    return random.choice(tetromino_set)()
