from utils.window_manager import window
from ui.button import Button
from ui.text import Text
from enum import Enum, auto
import utils.controller as controller
import settings.settings as s
import stats.high_score as high_score
from ui.menu.start_menu import StartMenu


class Menu:
    class MenuState(Enum):
        MAIN = auto()
        START = auto()
        SCORE = auto()

    class ButtonPos(Enum):
        PLAY = auto()
        SCORE = auto()
        QUIT = auto()

    def __init__(self):
        self.btn = self.ButtonPos.PLAY
        self.state = self.MenuState.MAIN
        self.main_screen = []
        self.score_screen = []
        self.main_screen.append(Button("PLAY", self.ButtonPos.PLAY, 50, s.win_w * s.scale / 2, 130 * s.scale, window))
        self.main_screen.append(Button("SCORE", self.ButtonPos.SCORE, 30, s.win_w * s.scale / 2, 200 * s.scale, window))
        self.main_screen.append(Button("QUIT", self.ButtonPos.QUIT, 30, s.win_w * s.scale / 2, 250 * s.scale, window))
        self.update_score()

        self.start_menu = StartMenu()

    def update(self):
        """
        :return 0: no redraw
        :return 1: need redraw
        :return 2: to play
        :return 9: quit
        """
        result = 0
        if controller.just_pressed["Clear"] and self.state != self.MenuState.MAIN:
            self.state = self.MenuState.MAIN
            result = 1
        if self.state == self.MenuState.MAIN:
            if controller.just_pressed["Start"]:
                if self.btn == self.ButtonPos.QUIT:
                    return 9
                elif self.btn == self.ButtonPos.PLAY:
                    self.state = self.MenuState.START
                    result = 1
                elif self.btn == self.ButtonPos.SCORE:
                    self.state = self.MenuState.SCORE
                    result = 1
            result = max(result, self.change_state())
        elif self.state == self.MenuState.START:
            result = max(self.start_menu.update(), result)
        if result == 2:
            self.state = self.MenuState.MAIN
            return 2
        return result

    def update_score(self):
        self.score_screen = []
        self.score_screen.append(Text("High scores:", (200, 200, 200), 30, s.win_w / 2, 50))
        for i, score in enumerate(high_score.table.score_list):
            self.score_screen.append(Text((score[0] + ": " + str(score[1])) if score[1] != 0 else "...vacant..."
                                          , (200, 200, 200), 20, s.win_w / 2, 100+(i+1)*30))

    def draw(self):
        if self.state == self.MenuState.MAIN:
            for i in self.main_screen:
                i.draw(self.btn)
        elif self.state == self.MenuState.SCORE:
            for i in self.score_screen:
                i.draw()
        elif self.state == self.MenuState.START:
            self.start_menu.draw()

    def change_state(self):
        if controller.just_pressed["Down"]:
            if self.btn == self.ButtonPos.PLAY:
                self.btn = self.ButtonPos.SCORE
            elif self.btn == self.ButtonPos.SCORE:
                self.btn = self.ButtonPos.QUIT
            return 1
        elif controller.just_pressed["Up"]:
            if self.btn == self.ButtonPos.QUIT:
                self.btn = self.ButtonPos.SCORE
            elif self.btn == self.ButtonPos.SCORE:
                self.btn = self.ButtonPos.PLAY
            return 1
        return 0
