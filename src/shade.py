import well
import data.settings as s
from tetromino.tetromino import Tetromino
import t_draw


shade: Tetromino


def update_pos(player: Tetromino) -> None:
    shade.position.x = player.position.x
    shade.position.y = player.position.y
    if player.state == 0:
        shade.set_0_rotation()
    elif player.state == 1:
        shade.set_1_rotation()
    elif player.state == 2:
        shade.set_2_rotation()
    elif player.state == 3:
        shade.set_3_rotation()

    while move_down() != 1:
        pass


def move_down():
    for i in shade.body:
        cell_x = i.position.x // s.CELL_SIZE
        cell_y = i.position.y // s.CELL_SIZE + 1
        if cell_y >= len(well.well) - 1:
            return 1
        if well.well[cell_y][cell_x - 1]:
            return 1
    for i in shade.body:
        i.position.y += s.CELL_SIZE
    shade.position.y += s.CELL_SIZE


def draw():
    for i in shade.body:
        t_draw.shade(i.position.x, i.position.y)
