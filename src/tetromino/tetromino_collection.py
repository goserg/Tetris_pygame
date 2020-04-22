from tetromino.tetromino import Tetromino
from utils.dataclasses_ import Position
import data.settings as s


class TypeI(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(4 * s.CELL_SIZE, -s.CELL_SIZE)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeI"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 3 * s.CELL_SIZE, y + s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2 * s.CELL_SIZE, y)
        self._two.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + 3 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + 2 * s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + 3 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 3 * s.CELL_SIZE)


class TypeJ(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5 * s.CELL_SIZE, -s.CELL_SIZE)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeJ"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + 2 * s.CELL_SIZE, y)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)


class TypeL(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5 * s.CELL_SIZE, -s.CELL_SIZE)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeL"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x, y + 2 * s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x + s.CELL_SIZE, y)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2 * s.CELL_SIZE, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)


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
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y)
        self._four.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)

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
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + 2 * s.CELL_SIZE, y)
        self._three.position = Position(x, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._two.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)


class TypeT(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.position = Position(5 * s.CELL_SIZE, -s.CELL_SIZE)
        self.set_0_rotation()
        for i in self.body:
            i.color_tag = "TypeT"

    def set_0_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)


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
        self._two.position = Position(x + s.CELL_SIZE, y)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)

    def set_1_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + 2 * s.CELL_SIZE, y)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + 2 * s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_2_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x, y + s.CELL_SIZE)
        self._two.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + 2 * s.CELL_SIZE)
        self._four.position = Position(x + 2 * s.CELL_SIZE, y + 2 * s.CELL_SIZE)

    def set_3_rotation(self) -> None:
        x = self.position.x
        y = self.position.y
        self._one.position = Position(x + s.CELL_SIZE, y)
        self._two.position = Position(x, y + s.CELL_SIZE)
        self._three.position = Position(x + s.CELL_SIZE, y + s.CELL_SIZE)
        self._four.position = Position(x, y + 2 * s.CELL_SIZE)
