from cube import Cube
import settings.settings as s
import level


class Border:
    def __init__(self):
        self.color_tag = "Border"
        self.generate_border()

    def generate_border(self):
        cols = s.game_w // s.cell_size
        rows = s.game_h // s.cell_size
        for i in range(0, cols-2):
            cube = Cube("Wall", (i+1, 0), self.color_tag)
            level.add(cube)
            cube = Cube("Wall", (i+1, rows - 1), self.color_tag)
            level.add(cube)
        for i in range(0, rows):
            cube = Cube("Wall", (0, i), self.color_tag)
            level.add(cube)
            cube = Cube("Wall", (cols-1, i), self.color_tag)
            level.add(cube)

