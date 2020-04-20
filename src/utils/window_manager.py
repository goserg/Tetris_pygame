import data.settings as s
import pygame

window = pygame.display.set_mode((int(s.WIN_W * s.scale), int(s.WIN_H * s.scale)))
pygame.display.set_caption(" ".join((s.NAME, s.VERSION)))
