import well
from tetromino.tetromino import Tetromino


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
        x = i.position.x
        y = i.position.y + 1
        if y > 23:
            return 1
        for j in well.cubes:
            if j.position.x == x and j.position.y == y:
                return 1
    for i in shade.body:
        i.position.y += 1
    shade.position.y += 1


def draw():
    for i in shade.body:
        i.draw_shade()
