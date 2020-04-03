import tetromino.generator
import tetromino.collection

next_one = None


def change():
    global next_one
    next_one = tetromino.generator.get_new()
    if not next_one:
        return None
    if type(next_one) == tetromino.collection.TypeI:
        next_one.pos = (15.5, 2)
    elif type(next_one) == tetromino.collection.TypeO:
        next_one.pos = (16.5, 2)
    else:
        next_one.pos = (16, 2)
    next_one.set_0_rotation()


change()
