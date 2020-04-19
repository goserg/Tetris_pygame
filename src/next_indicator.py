import tetromino.generator
import tetromino.collection
from tetromino.tetromino import Tetromino
from utils.dataclasses_ import Position

next_one: Tetromino


def change() -> None:
    global next_one
    next_one = tetromino.generator.get_new()
    if not next_one:
        return None
    if type(next_one) == tetromino.collection.TypeI:
        next_one.position = Position(12.5, 2)
    elif type(next_one) == tetromino.collection.TypeO:
        next_one.position = Position(13.5, 2)
    else:
        next_one.position = Position(13, 2)
    next_one.set_0_rotation()


change()
