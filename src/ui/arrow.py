from utils.window_manager import window
import utils.controller as controller
import settings.settings as s
import pygame


class Arrow:
    def __init__(self, x, y, size, horizontal=True, flip=False, tag=None):
        self.x = x
        self.y = y
        self.size = size
        self.color = (100, 100, 100)
        self.selected = False
        self.flip = flip
        self.horizontal = horizontal
        self.tag = tag

    def update(self):
        """

        :return True: if updated
        """
        if self.tag:
            if controller.pressed[self.tag]:
                self.color = (255, 255, 255)
                return True
            else:
                if self.color != (100, 100, 100):
                    self.color = (100, 100, 100)
                    return True
        return False

    def draw(self):
        x = self.x * s.scale
        y = self.y * s.scale
        size = self.size * s.scale

        if self.horizontal:
            pygame.draw.polygon(window, self.color,
                                ((x, y + size / 2),
                                 (x, y - size / 2),
                                 (x + (size if self.flip else -size) / 2, y)))
        else:
            pygame.draw.polygon(window, self.color,
                                ((x - size / 2, y),
                                 (x + size / 2, y),
                                 (x, y + (size if self.flip else -size) / 2)))
