from ui.text import Text
from ui.ui_block import UIBlock
from ui.name_input import NameInput
import settings.settings as s
from utils.fsm import GameState


class UI:
    def __init__(self):
        self.text_color = (200, 200, 200)
        self.next_text = Text("next", self.text_color, 20, 290, 20)
        self.lines_cleared_block = UIBlock(290, 120)
        self.lines_cleared_block.add(Text("cleared", self.text_color, 20, 0, 0))
        self.lines_cleared_block.add(Text("0", self.text_color, 20, 0, 0))
        self.score_block = UIBlock(290, 180)
        self.score_block.add(Text("score", self.text_color, 20, 0, 0))
        self.score_block.add(Text("0", self.text_color, 20, 0, 0))
        self.level_block = UIBlock(290, 240)
        self.level_block.add(Text("level", self.text_color, 20, 0, 0))
        self.level_block.add(Text("0", self.text_color, 20, 0, 0))

        self.pause = Text("PAUSE", (255, 255, 255), 20,
                          s.game_w // 2,
                          s.game_h // 2)
        self.game_over = Text("GAME OVER", (255, 255, 255), 20,
                          s.game_w // 2,
                          s.game_h // 2)

        self.score_plate = NameInput()

    def draw(self, state):
        self.next_text.draw()
        self.lines_cleared_block.draw()
        self.score_block.draw()
        self.level_block.draw()
        if state == GameState.GAME_OVER_RECORD:
            self.score_plate.draw()
        elif state == GameState.GAME_OVER:
            self.game_over.draw()
        elif state == GameState.PAUSE:
            self.pause.draw()


ui = UI()
