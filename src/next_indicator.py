import tetromino.generator
import tetromino.tetromino_collection
from tetromino.tetromino import Tetromino
import data.settings as s
from utils.dataclasses_ import Position
import t_draw

next_one: Tetromino
x = 0
y = 40


def change() -> None:
    global next_one, x
    next_one = tetromino.generator.get_new()
    next_one.position = Position(0, 0)
    next_one.set_0_rotation()

    if type(next_one) == tetromino.tetromino_collection.TypeI:
        x = 250
    elif type(next_one) == tetromino.tetromino_collection.TypeO:
        x = 270
    else:
        x = 260


def draw():
    for i in next_one.body:
        t_draw.cube(x + i.position.x, y + i.position.y, i.color_tag)


change()
