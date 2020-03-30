import utils.settings as s
from utils.window_manager import window
import pygame


class Cube:

    def __init__(self, position, color):
        self.color = color
        self.position = position

    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0] * s.cell_size * s.scale,
                                              self.position[1] * s.cell_size * s.scale,
                                              s.cell_size * s.scale, s.cell_size * s.scale))
