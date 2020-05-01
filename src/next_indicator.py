import tetromino.generator
import tetromino.tetromino_collection
from tetromino.tetromino import Tetromino
from utils.dataclasses_ import Position
import draw_manager

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
        draw_manager.cube(x + i.position.x, y + i.position.y, i.color_tag)


change()
