import tetromino.generator

next_one = None


def change():
    global next_one
    next_one = tetromino.generator.get_new()
    if not next_one:
        return None
    next_one.pos = (16, 2)
    next_one.set_0_rotation()


change()
