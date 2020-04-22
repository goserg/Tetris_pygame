from utils.dataclasses_ import Cube, Position
import data.settings as s
import well


class Border:
    def __init__(self) -> None:
        self.color_tag = "Border"
        self.generate_border()

    def generate_border(self) -> None:
        for i in range(0, s.COLUMNS * s.CELL_SIZE, s.CELL_SIZE):
            cube = Cube(
                Position(i + 1 * s.CELL_SIZE, (s.ROWS - 1) * s.CELL_SIZE),
                self.color_tag,
            )
            well.border.append(cube)
        for i in range(-1 * s.CELL_SIZE, s.ROWS * s.CELL_SIZE, s.CELL_SIZE):
            cube = Cube(Position(0, i), self.color_tag)
            well.border.append(cube)
            cube = Cube(Position((s.COLUMNS + 1) * s.CELL_SIZE, i), self.color_tag)
            well.border.append(cube)
