from cube import Cube
import settings.settings as s
import well
from utils.dataclasses_ import Position


class Border:
    def __init__(self) -> None:
        self.color_tag = "Border"
        self.generate_border()

    def generate_border(self) -> None:
        cols = s.game_w // s.cell_size
        rows = s.game_h // s.cell_size
        for i in range(0, cols - 2):
            cube = Cube("Wall", Position(i + 1, rows - 1), self.color_tag)
            well.add(cube)
        for i in range(-1, rows):
            cube = Cube("Wall", Position(0, i), self.color_tag)
            well.add(cube)
            cube = Cube("Wall", Position(cols - 1, i), self.color_tag)
            well.add(cube)
