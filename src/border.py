from cube import Cube
import settings.settings as s
import well


class Border:
    def __init__(self):
        self.color_tag = "Border"
        self.generate_border()

    def generate_border(self):
        cols = s.game_w // s.cell_size
        rows = s.game_h // s.cell_size
        for i in range(0, cols-2):
            cube = Cube("Wall", (i+1, rows - 1), self.color_tag)
            well.add(cube)
        for i in range(-1, rows):
            cube = Cube("Wall", (0, i), self.color_tag)
            well.add(cube)
            cube = Cube("Wall", (cols-1, i), self.color_tag)
            well.add(cube)

