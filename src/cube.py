import utils.settings as s
from utils.window_manager import window
import pygame


def color_bottom(i):
    return int(i * 0.5)


def color_side(i):
    return int(i * 0.9)


def color_top(i):
    if i == 0:
        return 179
    elif i == 240:
        return 251
    elif i == 160:
        return 227
    return i


class Cube:

    def __init__(self, position, color, tag):
        self.color = color
        self.position = position
        self.tag = tag

    def draw_shade(self):
        x = self.position[0] * s.cell_size * s.scale
        y = self.position[1] * s.cell_size * s.scale
        size = s.cell_size * s.scale
        pygame.draw.rect(window, (20, 20, 20), (x, y, size, size))

    def draw(self):
        x = self.position[0] * s.cell_size * s.scale
        y = self.position[1] * s.cell_size * s.scale
        size = s.cell_size * s.scale
        pygame.draw.rect(window, self.color, (x, y, size, size))

        if not s.flat:
            top_color = (color_top(self.color[0]), color_top(self.color[1]), color_top(self.color[2]))
            pygame.draw.polygon(window, top_color, ((x, y),
                                                    (x + size, y),
                                                    (x + size * 7 / 8, y + size / 8),
                                                    (x + size / 8, y + size / 8)))
            bottom_color = (color_bottom(self.color[0]), color_bottom(self.color[1]), color_bottom(self.color[2]))
            pygame.draw.polygon(window, bottom_color, ((x, y + size),
                                                       (x + size, y + size),
                                                       (x + size * 7 / 8, y + size * 7 / 8),
                                                       (x + size / 8, y + size * 7 / 8)))
            side_color = (color_side(self.color[0]), color_side(self.color[1]), color_side(self.color[2]))
            pygame.draw.polygon(window, side_color, ((x, y),
                                                     (x, y + size),
                                                     (x + size / 8, y + size * 7 / 8),
                                                     (x + size / 8, y + size / 8)))
            pygame.draw.polygon(window, side_color, ((x + size, y),
                                                     (x + size, y + size),
                                                     (x + size * 7 / 8, y + size * 7 / 8),
                                                     (x + size * 7 / 8, y + size / 8)))
