from tetromino.tetromino import Tetromino
from utils.dataclasses_ import Position


class TypeI(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(4, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeI"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 1)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 3, y + 1)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2, y)
        self._two.position = Position(x + 2, y + 1)
        self._three.position = Position(x + 2, y + 2)
        self._four.position = Position(x + 2, y + 3)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 2)
        self._two.position = Position(x + 1, y + 2)
        self._three.position = Position(x + 2, y + 2)
        self._four.position = Position(x + 3, y + 2)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 1, y + 2)
        self._four.position = Position(x + 1, y + 3)


class TypeJ(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeJ"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 1)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 2, y + 2)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x, y + 2)
        self._four.position = Position(x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 2, y)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 1, y + 2)


class TypeL(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeL"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 1)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x, y + 2)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x + 1, y)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 1, y + 2)
        self._four.position = Position(x + 2, y + 2)


class TypeO(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeO"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y)
        self._four.position = Position(x + 1, y + 1)

    def _try_rotation(self) -> bool:
        return False

    def _wall_push_rotation(self) -> bool:
        return False


class TypeS(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeS"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 2, y)
        self._three.position = Position(x, y + 1)
        self._four.position = Position(x + 1, y + 1)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 2, y + 2)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y + 1)
        self._two.position = Position(x + 2, y + 1)
        self._three.position = Position(x, y + 2)
        self._four.position = Position(x + 1, y + 2)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 1, y + 2)


class TypeT(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5, -1)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeT"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 1)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 1, y + 2)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 2, y + 1)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 1, y + 2)


class TypeZ(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeZ"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x + 1, y)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x + 2, y + 1)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2, y)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 2, y + 1)
        self._four.position = Position(x + 1, y + 2)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 1)
        self._two.position = Position(x + 1, y + 1)
        self._three.position = Position(x + 1, y + 2)
        self._four.position = Position(x + 2, y + 2)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 1, y)
        self._two.position = Position(x, y + 1)
        self._three.position = Position(x + 1, y + 1)
        self._four.position = Position(x, y + 2)
