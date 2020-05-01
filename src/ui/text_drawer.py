import pygame

import data.settings as s
import utils.window_manager
from utils.dataclasses_ import Position


def display_text(text: str, color: tuple, size: int, position: Position) -> None:
    size = int(size * s.scale)
    font = pygame.font.SysFont(s.FONT, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (position.x * s.scale, position.y * s.scale)
    utils.window_manager.window.blit(text_surf, text_rect)
