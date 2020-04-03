import settings.settings as s
import pygame

window = pygame.display.set_mode((int(s.win_w * s.scale), int(s.win_h * s.scale)))
pygame.display.set_caption(" ".join((s.name, s.version)))

