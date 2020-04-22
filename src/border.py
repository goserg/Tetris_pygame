import data.settings as s
import t_draw
from utils.dataclasses_ import Position
from typing import List


class Border:
    __slots__ = ("color_tag", "positions")

    def __init__(self) -> None:
        self.color_tag = "Border"
        self.positions: List[Position] = []
        self.generate_floor()
        self.generate_sides()

    def generate_floor(self) -> None:
        for i in range(0, s.COLUMNS * s.CELL_SIZE, s.CELL_SIZE):
            self.positions.append(Position(i + 1 * s.CELL_SIZE, (s.ROWS - 1) * s.CELL_SIZE))

    def generate_sides(self) -> None:
        for i in range(-1 * s.CELL_SIZE, s.ROWS * s.CELL_SIZE, s.CELL_SIZE):
            self.positions.append(Position(0, i))
            self.positions.append(Position((s.COLUMNS + 1) * s.CELL_SIZE, i))

    def draw(self) -> None:
        for i in self.positions:
            t_draw.cube(i.x, i.y, self.color_tag)
