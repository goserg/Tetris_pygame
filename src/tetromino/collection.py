from cube import Cube
from tetromino.tetromino import Tetromino


class TypeI(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (0, 240, 240)
        up = Cube((self.head.position[0], self.head.position[1] - 1), self.head.color)
        down = Cube((self.head.position[0], self.head.position[1] + 1), self.head.color)
        down2 = Cube((self.head.position[0], self.head.position[1] + 2), self.head.color)
        self.body.append(up)
        self.body.append(down)
        self.body.append(down2)


class TypeJ(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (0, 0, 240)
        right = Cube((self.head.position[0] + 1, self.head.position[1]), self.head.color)
        left = Cube((self.head.position[0] - 1, self.head.position[1]), self.head.color)
        up_left = Cube((self.head.position[0] - 1, self.head.position[1] - 1), self.head.color)
        self.body.append(right)
        self.body.append(left)
        self.body.append(up_left)


class TypeL(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (240, 160, 0)
        right = Cube((self.head.position[0] + 1, self.head.position[1]), self.head.color)
        left = Cube((self.head.position[0] - 1, self.head.position[1]), self.head.color)
        up_right = Cube((self.head.position[0] + 1, self.head.position[1] - 1), self.head.color)
        self.body.append(right)
        self.body.append(left)
        self.body.append(up_right)


class TypeO(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (240, 240, 0)
        up = Cube((self.head.position[0], self.head.position[1] - 1), self.head.color)
        right = Cube((self.head.position[0] + 1, self.head.position[1]), self.head.color)
        up_right = Cube((self.head.position[0] + 1, self.head.position[1] - 1), self.head.color)
        self.body.append(up)
        self.body.append(right)
        self.body.append(up_right)


class TypeS(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (0, 240, 0)
        left = Cube((self.head.position[0] - 1, self.head.position[1]), self.head.color)
        up = Cube((self.head.position[0], self.head.position[1] - 1), self.head.color)
        up_right = Cube((self.head.position[0] + 1, self.head.position[1] - 1), self.head.color)
        self.body.append(left)
        self.body.append(up)
        self.body.append(up_right)


class TypeT(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (160, 0, 240)
        up = Cube((self.head.position[0], self.head.position[1] - 1), self.head.color)
        right = Cube((self.head.position[0] + 1, self.head.position[1]), self.head.color)
        left = Cube((self.head.position[0] - 1, self.head.position[1]), self.head.color)
        self.body.append(up)
        self.body.append(right)
        self.body.append(left)


class TypeZ(Tetromino):
    def __init__(self):
        super().__init__()
        self.head.color = (240, 0, 0)
        right = Cube((self.head.position[0] + 1, self.head.position[1]), self.head.color)
        up = Cube((self.head.position[0], self.head.position[1] - 1), self.head.color)
        up_left = Cube((self.head.position[0] - 1, self.head.position[1] - 1), self.head.color)
        self.body.append(right)
        self.body.append(up)
        self.body.append(up_left)
