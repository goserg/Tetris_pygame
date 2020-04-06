import pygame
import settings.settings as s
from utils.window_manager import window


def display_text(text, color, size, x, y):
    size = int(size * s.scale)
    font = pygame.font.Font(s.font, size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (x * s.scale, y * s.scale)
    window.blit(text_surf, text_rect)
