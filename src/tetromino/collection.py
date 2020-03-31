from cube import Cube
from tetromino.tetromino import Tetromino


class TypeI(Tetromino):
    def __init__(self):
        super().__init__()
        self.color = (0, 240, 240)
        self.pos = (5, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_1_rotation()
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

        self.state = 1

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
        self.color = (0, 0, 240)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
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
        self.color = (240, 160, 0)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
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
        self.color = (240, 240, 0)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
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
        self.color = (0, 240, 0)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)
        self.state = 0

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
        self.color = (160, 0, 240)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
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
        self.color = (240, 0, 0)
        self.pos = (6, 1)
        self.one = Cube(self.pos, self.color, "block")
        self.two = Cube(self.pos, self.color, "block")
        self.three = Cube(self.pos, self.color, "block")
        self.four = Cube(self.pos, self.color, "block")
        self.set_0_rotation()
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
