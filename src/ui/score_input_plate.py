from enum import Enum, auto
from ui.button import Button
from ui.text import Text
import settings.settings as s
from utils.window_manager import window
import pygame

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class ScorePlate:
    def __init__(self):
        self.name = "enter your name"
        self.letter = "A"
        self.buttons = []
        self.plate = pygame.Surface((300 * s.scale, 300 * s.scale))

        self.game_over = Text("GAME OVER", (255, 255, 255), 30,
                              s.win_w // 2,
                              s.win_h // 4)
        self.name_text = Text(self.name, (255, 255, 255), 30,
                              s.win_w // 2,
                              s.win_h * 2 // 4)
        self.press_a_btn = Text("A to select letter", (255, 255, 255), 15,
                                s.win_w // 2,
                                s.win_h * 3 // 4)
        self.press_start_btn = Text("Start to confirm", (255, 255, 255), 15,
                                    s.win_w // 2,
                                    s.win_h * 3 // 4 + 15)
        self.press_b_btn = Text("B to clear name", (255, 255, 255), 15,
                                s.win_w // 2,
                                s.win_h * 3 // 4 + 30)
        for i, l in enumerate(letters):
            self.buttons.append(Button(l, l, 5 * s.scale, i * 11 * s.scale + 25, 150, self.plate))

    def draw(self):
        self.plate.fill((50, 50, 50))
        for i in self.buttons:
            i.draw(self.letter)

        surf_rect = self.plate.get_rect()
        surf_rect.center = (s.win_w * s.scale / 2, s.win_h * s.scale / 2)
        window.blit(self.plate, surf_rect)

        self.game_over.draw()
        self.name_text.draw()
        self.press_a_btn.draw()
        self.press_start_btn.draw()
        self.press_b_btn.draw()

    def move(self, direction):
        """

        :param direction: tuple: controls direction
        :return: 0 if not moved else 1
        """
        if direction[0] == 0:
            return 0
        index = letters.index(self.letter) + direction[0]
        if index < 0:
            index = len(letters) - 1
        if index >= len(letters):
            index = 0
        self.letter = letters[index]
        return 1

    def add_letter(self):
        if self.name == "enter your name":
            self.name = self.letter
        elif len(self.name) < 10:
            self.name += self.letter
        self.name_text.text = self.name

    def clear_name(self):
        self.name = "enter your name"
        self.name_text.text = self.name

    def get_name(self):
        if self.name == "enter your name":
            return "anonymous"
        return self.name
