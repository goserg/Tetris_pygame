import utils.settings as s
from utils.window_manager import window
import pygame


def color_darker(i, percent):
    r = i[0] * percent
    g = i[1] * percent
    b = i[2] * percent
    return r, g, b


def color_brighten(i, percent):
    r = i[0] + (256-i[0]) * percent
    g = i[1] + (256-i[1]) * percent
    b = i[2] + (256-i[2]) * percent
    return r, g, b


class Cube:

    def __init__(self, position, color, tag):
        self.color = color
        self.position = position
        self.tag = tag

    def draw_shade(self):
        x = self.position[0] * s.cell_size * s.scale
        y = self.position[1] * s.cell_size * s.scale
        size = s.cell_size * s.scale
        pygame.draw.rect(window, s.colors["Shade"], (x, y, size, size))

    def draw(self):
        x = self.position[0] * s.cell_size * s.scale
        y = self.position[1] * s.cell_size * s.scale
        size = s.cell_size * s.scale
        pygame.draw.rect(window, self.color, (x, y, size, size))

        if not s.flat:
            top_color = (color_brighten(self.color, 0.7))
            pygame.draw.polygon(window, top_color, ((x, y),
                                                    (x + size, y),
                                                    (x + size * 7 / 8, y + size / 8),
                                                    (x + size / 8, y + size / 8)))
            bottom_color = (color_darker(self.color, 0.6))
            pygame.draw.polygon(window, bottom_color, ((x, y + size),
                                                       (x + size, y + size),
                                                       (x + size * 7 / 8, y + size * 7 / 8),
                                                       (x + size / 8, y + size * 7 / 8)))
            side_color = (color_darker(self.color, 0.9))
            pygame.draw.polygon(window, side_color, ((x, y),
                                                     (x, y + size),
                                                     (x + size / 8, y + size * 7 / 8),
                                                     (x + size / 8, y + size / 8)))
            pygame.draw.polygon(window, side_color, ((x + size, y),
                                                     (x + size, y + size),
                                                     (x + size * 7 / 8, y + size * 7 / 8),
                                                     (x + size * 7 / 8, y + size / 8)))
        else:
            pygame.draw.lines(window, s.colors["Grid"], True, [(x, y),
                                                               (x + size, y),
                                                               (x + size, y + size),
                                                               (x, y + size)])
