from cube import Cube
import utils.settings as s
import level


class Border:
    def __init__(self):
        self.color = s.border_color
        self.generate_border()

    def generate_border(self):
        cols = s.win_w//s.cell_size
        rows = s.win_h//s.cell_size
        for i in range(0, cols-2):
            cube = Cube((i+1, 0), self.color)
            level.add(cube)
            cube = Cube((i+1, rows - 1), self.color)
            level.add(cube)
        for i in range(0, rows):
            cube = Cube((0, i), self.color)
            level.add(cube)
            cube = Cube((cols-1, i), self.color)
            level.add(cube)

