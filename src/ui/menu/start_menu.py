import stats.high_score as save
import utils.controller as controller
from ui.text import Text
import stats.score
import settings.settings as s

from ui.switcher_button import SwitcherButton

from ui.menu.name_input import NameInput

import stats.level


class StartMenu:
    def __init__(self):
        self.move_timer = 0
        self.text = Text("select player", (200, 200, 200), 30, s.win_w / 2, 50)
        self.text2 = Text("Y to change current player name", (200, 200, 200), 15, s.win_w / 2, 75)

        self.name_input = NameInput()
        self.name_input_enabled = False

        self.player_button = SwitcherButton(save.table.players, 0, (200, 200, 200), 20,
                                            s.win_w / 4 + 20, s.win_h / 2,
                                            horizontal=True)
        self.level_button = SwitcherButton(list(map(str, range(31))), 0, (200, 200, 200), 20,
                                           s.win_w * 3 / 4, s.win_h / 2,
                                           horizontal=False)

    def update(self):
        """

        :return 0: no change
        :return 1: need redraw
        :return 2: to play
        """

        if self.name_input_enabled:
            if controller.just_pressed["Pause"]:
                name = self.name_input.get_name()
                save.table.change_name(name, self.player_button.get_index())
                self.player_button.set_options(save.table.players)
                self.name_input_enabled = False
                return 1
            elif self.name_input.update():
                return 1
        else:
            if controller.is_Y_pressed():
                self.name_input_enabled = True
                self.name_input.set_name(self.player_button.get_text())
                return 1
            if self.player_button.update():
                return 1
            if self.level_button.update():
                return 1
            elif controller.just_pressed["Clear"]:
                self.name_input_enabled = False
                return 1
            elif controller.just_pressed["Start"]:
                stats.level.set_level(int(self.level_button.get_text()) * 10)
                stats.score.player_name = self.player_button.get_text()
                return 2
        if all(not value for value in controller.just_pressed.values()):
            return 0
        return 1

    def draw(self):
        self.text.draw()
        self.text2.draw()

        if self.name_input_enabled:
            self.name_input.draw()

        else:
            self.player_button.draw()
            self.level_button.draw()
