import stats.high_score as save
import utils.controller as controller
from ui.text import Text
import settings.settings as s

from ui.name_input import NameInput


class StartMenu:
    def __init__(self):
        self.move_timer = 0
        self.text = Text("select player", (200, 200, 200), 30, s.win_w / 2, 50)
        self.text2 = Text("Y to change current player name", (200, 200, 200), 15, s.win_w / 2, 75)
        self.text3 = Text("left, right to switch player", (200, 200, 200), 15, s.win_w / 2, 90)

        self.name_index = 0
        self.player = Text(save.table.players[self.name_index], (200, 200, 200), 20, s.win_w / 2, 250)
        self.name_input = NameInput()
        self.name_input_enabled = False

    def update(self):
        """

        :return 0: no change
        :return 1: to play
        :return 2: need redraw
        :return 9: back
        """
        if self.name_input_enabled:
            if controller.just_pressed["Start"]:
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
            elif controller.is_Y_pressed():
                self.name_input_enabled = True
                self.name_input.set_name(self.player.text)
                return 2
            elif controller.just_pressed["Clear"]:
                self.name_input_enabled = False
                return 9
            elif controller.just_pressed["Start"]:
                return 1

        if all(not value for value in controller.just_pressed.values()):
            return 0
        return 2

    def draw(self):
        self.text.draw()
        self.text2.draw()
        self.text3.draw()

        self.player.draw()

        if self.name_input_enabled:
            self.name_input.draw()
