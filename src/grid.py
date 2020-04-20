from utils.window_manager import window
import data.settings as s
import pygame


class Grid:
    def __init__(self) -> None:
        self.rows = s.GAME_H // s.CELL_SIZE
        self.cols = s.GAME_W // s.CELL_SIZE

    def draw(self) -> None:
        x = 0
        for _ in range(self.cols):
            x += s.CELL_SIZE * s.scale
            pygame.draw.line(
                window, s.color_scheme["Grid"], (x, 0), (x, s.GAME_H * s.scale)
            )
            pass

        y = 0
        for _ in range(self.rows):
            y += s.CELL_SIZE * s.scale

            pygame.draw.line(
                window, s.color_scheme["Grid"], (0, y), (s.GAME_W * s.scale, y)
            )
