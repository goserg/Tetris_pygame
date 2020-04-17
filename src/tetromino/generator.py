import random
from tetromino.collection import *

tetromino_set = (TypeI, TypeJ, TypeL, TypeO, TypeS, TypeT, TypeZ)


def get_new() -> Tetromino:
    return random.choice(tetromino_set)()
