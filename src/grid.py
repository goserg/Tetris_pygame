from utils.window_manager import window
import settings.settings as s
import pygame


class Grid:
    def __init__(self) -> None:
        self.rows = s.game_h // s.cell_size
        self.cols = s.game_w // s.cell_size

    def draw(self) -> None:
        x = 0
        for _ in range(self.cols):
            x += s.cell_size * s.scale
            pygame.draw.line(window, s.colors["Grid"], (x, 0), (x, s.game_h * s.scale))
            pass

        y = 0
        for _ in range(self.rows):
            y += s.cell_size * s.scale

            pygame.draw.line(window, s.colors["Grid"], (0, y), (s.game_w * s.scale, y))
