import stats.high_score as save
import utils.controller as controller
from ui.text import Text
from ui.arrow import Arrow
import settings.settings as s

from ui.name_input import NameInput

import stats.level


class StartMenu:
    def __init__(self):
        self.move_timer = 0
        self.text = Text("select player", (200, 200, 200), 30, s.win_w / 2, 50)
        self.text2 = Text("Y to change current player name", (200, 200, 200), 15, s.win_w / 2, 75)

        self.name_index = 0
        self.player = Text(save.table.players[self.name_index], (200, 200, 200), 20, s.win_w / 4 + 20, s.win_h / 2)
        self.name_input = NameInput()
        self.name_input_enabled = False
        self.start_level = Text("0", (200, 200, 200), 20, s.win_w * 3 / 4, s.win_h / 2)

        self.ar1 = Arrow(s.win_w * 3 / 4, s.win_h / 2 - 20, 20, horizontal=False, flip=False, tag="Up")
        self.ar2 = Arrow(s.win_w * 3 / 4, s.win_h / 2 + 20, 20, horizontal=False, flip=True, tag="Down")
        self.ar3 = Arrow(s.win_w / 4 - 60 + 20, s.win_h / 2, 20, horizontal=True, flip=False, tag="Left")
        self.ar4 = Arrow(s.win_w / 4 + 60 + 20, s.win_h / 2, 20, horizontal=True, flip=True, tag="Right")
        self.arrows = [self.ar1, self.ar2, self.ar3, self.ar4]

    def update(self):
        """

        :return 0: no change
        :return 1: to play
        :return 2: need redraw
        :return 9: back
        """
        if self.name_input_enabled:
            if controller.just_pressed["Pause"]:
                name = self.name_input.get_name()
                save.table.change_name(name, self.name_index)
                self.player.text = name
                self.name_input_enabled = False
                return 2
            if self.name_input.update():
                return 2
        else:
            if controller.just_pressed["Right"]:
                self.name_index += 1
                if self.name_index >= len(save.table.players):
                    self.name_index = 0
                self.player.text = save.table.players[self.name_index]
            elif controller.just_pressed["Left"]:
                self.name_index -= 1
                if self.name_index < 0:
                    self.name_index = len(save.table.players) - 1
                self.player.text = save.table.players[self.name_index]
            elif controller.just_pressed["Up"]:
                self.start_level.text = str(int(self.start_level.text) + 1)
                if int(self.start_level.text) > 30:
                    self.start_level.text = "0"
            elif controller.just_pressed["Down"]:
                self.start_level.text = str(int(self.start_level.text) - 1)
                if int(self.start_level.text) < 0:
                    self.start_level.text = "30"
            elif controller.is_Y_pressed():
                self.name_input_enabled = True
                self.name_input.set_name(self.player.text)
                return 2
            elif controller.just_pressed["Clear"]:
                self.name_input_enabled = False
                return 9
            elif controller.just_pressed["Start"]:
                stats.level.set_level(int(self.start_level.text)*10)
                return 1
        for i in self.arrows:
            if i.update():
                return 2

        if all(not value for value in controller.just_pressed.values()):
            return 0
        return 2

    def draw(self):
        self.text.draw()
        self.text2.draw()

        self.start_level.draw()

        self.player.draw()

        if self.name_input_enabled:
            self.name_input.draw()
        else:
            for i in self.arrows:
                i.draw()
