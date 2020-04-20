from utils.dataclasses_ import Cube, Position
import data.settings as s
import well


class Border:
    def __init__(self) -> None:
        self.color_tag = "Border"
        self.generate_border()

    def generate_border(self) -> None:
        cols = s.GAME_W // s.CELL_SIZE
        rows = s.GAME_H // s.CELL_SIZE
        for i in range(0, cols - 2):
            cube = Cube(Position(i + 1, rows - 1), self.color_tag)
            well.border.append(cube)
        for i in range(-1, rows):
            cube = Cube(Position(0, i), self.color_tag)
            well.border.append(cube)
            cube = Cube(Position(cols - 1, i), self.color_tag)
            well.border.append(cube)
