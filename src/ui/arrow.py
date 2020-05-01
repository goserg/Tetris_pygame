import pygame

import utils.controller as controller
import utils.window_manager
from utils.dataclasses_ import Position
import data.settings as s


class Arrow:
    def __init__(
        self,
        position: Position,
        size: int,
        horizontal: bool = True,
        flip: bool = False,
        tag: str = None,
    ) -> None:
        self.position = position
        self.size = size
        self.color = (100, 100, 100)
        self.selected = False
        self.flip = flip
        self.horizontal = horizontal
        self.tag = tag

    def update(self) -> bool:
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

    def draw(self) -> None:
        x = self.position.x * s.scale
        y = self.position.y * s.scale
        size = self.size * s.scale

        if self.horizontal:
            pygame.draw.polygon(
                utils.window_manager.window,
                self.color,
                (
                    (x, y + size / 2),
                    (x, y - size / 2),
                    (x + (size if self.flip else -size) / 2, y),
                ),
            )
        else:
            pygame.draw.polygon(
                utils.window_manager.window,
                self.color,
                (
                    (x - size / 2, y),
                    (x + size / 2, y),
                    (x, y + (size if self.flip else -size) / 2),
                ),
            )
