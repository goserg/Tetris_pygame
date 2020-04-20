from utils.window_manager import window
from utils.fsm import MenuState
from ui.button import Button
from ui.text import Text
from enum import Enum
import utils.controller as controller
import data.settings as s
import stats.high_score as high_score
from ui.menu.start_menu import StartMenu


class Menu:
    class ButtonPos(Enum):
        PLAY = "play"
        SCORE = "score"
        QUIT = "quit"

    def __init__(self) -> None:
        self.btn = self.ButtonPos.PLAY
        self.state = MenuState.MAIN
        self.main_screen = []
        self.score_screen = []
        self.main_screen.append(
            Button(
                "PLAY",
                self.ButtonPos.PLAY.value,
                50,
                s.WIN_W * s.scale / 2,
                130 * s.scale,
                window,
            )
        )
        self.main_screen.append(
            Button(
                "SCORE",
                self.ButtonPos.SCORE.value,
                30,
                s.WIN_W * s.scale / 2,
                200 * s.scale,
                window,
            )
        )
        self.main_screen.append(
            Button(
                "QUIT",
                self.ButtonPos.QUIT.value,
                30,
                s.WIN_W * s.scale / 2,
                250 * s.scale,
                window,
            )
        )
        self.update_score()

        self.start_menu = StartMenu()

    def update(self) -> int:
        """
        :return 0: no redraw
        :return 1: need redraw
        :return 2: to play
        :return 9: quit
        """
        result = 0
        if (
            controller.just_pressed["Clear"]
            and self.state != MenuState.MAIN
            and not (
                self.state == MenuState.START and self.start_menu.name_input_enabled
            )
        ):
            self.state = MenuState.MAIN
            result = 1
        if self.state == MenuState.MAIN:
            if controller.just_pressed["Start"]:
                if self.btn == self.ButtonPos.QUIT:
                    return 9
                elif self.btn == self.ButtonPos.PLAY:
                    self.state = MenuState.START
                    result = 1
                elif self.btn == self.ButtonPos.SCORE:
                    self.state = MenuState.SCORE
                    result = 1
            result = max(result, self.change_state())
        elif self.state == MenuState.START:
            result = max(self.start_menu.update(), result)
        if result == 2:
            self.state = MenuState.MAIN
            return 2
        return result

    def update_score(self) -> None:
        self.score_screen = []
        self.score_screen.append(
            Text("High scores:", (200, 200, 200), 30, s.WIN_W / 2, 50)
        )
        for i, score in enumerate(high_score.score_list.score_list):
            self.score_screen.append(
                Text(
                    (score[0] + ": " + str(score[1]))
                    if score[1] != 0
                    else "...vacant...",
                    (200, 200, 200),
                    20,
                    s.WIN_W / 2,
                    100 + (i + 1) * 30,
                )
            )

    def draw(self) -> None:
        if self.state == MenuState.MAIN:
            for i in self.main_screen:
                i.draw(str(self.btn.value))
        elif self.state == MenuState.SCORE:
            for i in self.score_screen:
                i.draw()
        elif self.state == MenuState.START:
            self.start_menu.draw()

    def change_state(self) -> int:
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
