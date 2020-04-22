from ui.button import Button
from ui.text import Text
import data.settings as s
from utils.window_manager import window
import utils.controller as controller
import pygame
from utils.dataclasses_ import Position

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
MAX_NAME_LEN = 15


class NameInput:
    def __init__(self) -> None:
        self.name = "enter your name"
        self.letter = "A"
        self.buttons = []
        self.move_timer = 0
        self.plate = pygame.Surface((300 * s.scale, 300 * s.scale))

        self.game_over = Text(
            "Name change", (255, 255, 255), 30, Position(s.WIN_W // 2, s.WIN_H // 4)
        )
        self.name_text = Text(
            self.name, (255, 255, 255), 30, Position(s.WIN_W // 2, s.WIN_H * 2 // 4)
        )
        self.press_a_btn = Text(
            "A to select letter",
            (255, 255, 255),
            15,
            Position(s.WIN_W // 2, s.WIN_H * 3 // 4),
        )
        self.press_start_btn = Text(
            "Start to confirm",
            (255, 255, 255),
            15,
            Position(s.WIN_W // 2, s.WIN_H * 3 // 4 + 15),
        )
        self.press_b_btn = Text(
            "B to clear letter",
            (255, 255, 255),
            15,
            Position(s.WIN_W // 2, s.WIN_H * 3 // 4 + 30),
        )
        x0 = 0
        y0 = 0
        for letter in LETTERS:
            x = x0 * 15 * s.scale + 90 * s.scale
            y = y0 * 20 * s.scale + 75 * s.scale
            self.buttons.append(Button(letter, letter, 14, Position(x, y), self.plate))
            x0 += 1
            if x0 == 9:
                x0 = 0
                y0 += 1

    def update(self) -> bool:
        to_draw = False
        if self.move(controller.get_direction()) != 0:
            to_draw = True
        if controller.just_pressed["Start"]:
            self.add_letter()
            to_draw = True
        elif controller.just_pressed["Clear"]:
            self.remove_letter()
            to_draw = True
        return to_draw

    def draw(self) -> None:
        self.plate.fill((50, 50, 50))
        for i in self.buttons:
            i.draw(self.letter)

        surf_rect = self.plate.get_rect()
        surf_rect.center = (s.WIN_W * s.scale / 2, s.WIN_H * s.scale / 2)
        window.blit(self.plate, surf_rect)

        self.game_over.draw()
        self.name_text.draw()
        self.press_a_btn.draw()
        self.press_start_btn.draw()
        self.press_b_btn.draw()

    def move(self, direction: tuple) -> int:
        """

        :param direction: tuple: controls direction
        :return: 0 if not moved else 1
        """
        if self.move_timer > 0:
            self.move_timer -= 1
            return 0
        if direction == (0, 0):
            return 0
        self.move_timer = s.AUTO_SHIFT
        index = LETTERS.index(self.letter) + direction[0]
        if index < 0:
            index = len(LETTERS) - 1
        if index >= len(LETTERS):
            index = 0
        if direction[1] == 1:
            if 0 <= index < 8:
                index += 18
            else:
                index -= 9
        elif direction[1] == -1:
            if 18 <= index <= 26:
                index -= 18
            else:
                index += 9
        self.letter = LETTERS[index]
        return 1

    def add_letter(self) -> None:
        if self.name == "enter your name" and self.letter != " ":
            self.name = self.letter
        elif len(self.name) < MAX_NAME_LEN:
            self.name += self.letter
        self.name_text.text = self.name

    def remove_letter(self) -> None:
        if self.name == "enter your name":
            self.name_text.text = self.name
            return
        if len(self.name) == 1:
            self.name = "enter your name"
            self.name_text.text = self.name
            return
        self.name = self.name[:-1]
        self.name_text.text = self.name

    def get_name(self) -> str:
        if self.name == "enter your name":
            return "anonymous"
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
        self.name_text.text = name
