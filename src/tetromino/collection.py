from tetromino.tetromino import Tetromino


class TypeI(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.pos = (4, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeI"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 3, y + 1)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x + 2, y + 1)
        self.three.position = (x + 2, y + 2)
        self.four.position = (x + 2, y + 3)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 2)
        self.two.position = (x + 1, y + 2)
        self.three.position = (x + 2, y + 2)
        self.four.position = (x + 3, y + 2)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 1, y + 3)


class TypeJ(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.pos = (5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeJ"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 2, y + 2)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x, y + 2)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 2, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeL(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.pos = (5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeL"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x, y + 2)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x + 1, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 2, y + 2)


class TypeO(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeO"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y)
        self.four.position = (x + 1, y + 1)

    def try_rotation(self) -> int:
        return 0


class TypeS(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeS"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 2, y)
        self.three.position = (x, y + 1)
        self.four.position = (x + 1, y + 1)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 2, y + 2)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y + 1)
        self.two.position = (x + 2, y + 1)
        self.three.position = (x, y + 2)
        self.four.position = (x + 1, y + 2)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeT(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.pos = (5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeT"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)


class TypeZ(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeZ"

    def set_0_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y)
        self.two.position = (x + 1, y)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x + 2, y + 1)

    def set_1_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 2, y)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 2, y + 1)
        self.four.position = (x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x, y + 1)
        self.two.position = (x + 1, y + 1)
        self.three.position = (x + 1, y + 2)
        self.four.position = (x + 2, y + 2)

    def set_3_rotation(self) -> None:
        x = self.pos[0]
        y = self.pos[1]
        self.one.position = (x + 1, y)
        self.two.position = (x, y + 1)
        self.three.position = (x + 1, y + 1)
        self.four.position = (x, y + 2)
