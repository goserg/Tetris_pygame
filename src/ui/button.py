import pygame

from utils.dataclasses_ import Position
import data.settings as s


class Button:
    def __init__(
        self,
        text: str,
        tag: str,
        font_size: int,
        position: Position,
        surface: pygame.Surface,
    ) -> None:
        self.color = None
        self.font_size = font_size
        self.text = text
        self.position = position
        self.btn = tag
        self.surface = surface

        self.plate = pygame.Surface(
            (len(text) * font_size * s.scale, font_size * s.scale * 1.4)
        )

    def draw(self, btn: str) -> None:
        if self.btn == btn:
            self.color = (0, 0, 0)
            self.plate.fill((200, 200, 200))
        else:
            self.color = (100, 100, 100)
            self.plate.fill((0, 0, 0))
        size = int(self.font_size * s.scale)
        font = pygame.font.SysFont(s.FONT, size)
        text_surf = font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect()
        text_rect.center = (self.plate.get_width() // 2, self.plate.get_height() // 2)
        self.plate.blit(text_surf, text_rect)
        surf_rect = self.plate.get_rect()
        surf_rect.center = (self.position.x, self.position.y)

        self.surface.blit(self.plate, surf_rect)
