import pygame
import data.settings as s
from utils.window_manager import window


def display_text(text: str, color: tuple, size: int, x: int, y: int) -> None:
    size = int(size * s.scale)
    font = pygame.font.SysFont(s.FONT, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (x * s.scale, y * s.scale)
    window.blit(text_surf, text_rect)
