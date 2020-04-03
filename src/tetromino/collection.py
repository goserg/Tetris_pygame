from cube import Cube
from tetromino.tetromino import Tetromino
import utils.settings as s


class TypeI(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeI"]
        self.pos = (5, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_1_rotation()
        self.state = 1
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 3, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x + 2, y + 1)
        self.three.position = (x + 2, y + 2)
        self.four.position = (x + 2, y + 3)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 2)
        self.two.position = (x + 1, y + 2)
        self.three.position = (x + 2, y + 2)
        self.four.position = (x + 3, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 1, y + 3)


class TypeJ(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeJ"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 2, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 2, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x, y + 2)
        self.four.position = (x + 1, y + 2)


class TypeL(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeL"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 2, y + 2)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x + 1, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeO(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeO"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y)
        self.four.position = (x + 1, y + 1)

    def set_1_rotation(self):
        self.set_0_rotation()

    def set_2_rotation(self):
        self.set_0_rotation()

    def set_3_rotation(self):
        self.set_0_rotation()


class TypeS(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeS"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 2, y)
        self.three.position = (x, y + 1)
        self.four.position = (x + 1, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 2, y + 2)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y + 1)
        self.two.position = (x + 2, y + 1)
        self.three.position = (x, y + 2)
        self.four.position = (x + 1, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeT(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeT"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeZ(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = s.colors["TypeZ"]
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.state = 0
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

    def set_0_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x + 1, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_1_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 2, y + 2)

    def set_3_rotation(self):
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x, y + 2)
