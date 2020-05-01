from ui.text import Text
from ui.ui_block import UIBlock
from ui.menu.name_input import NameInput
import data.settings as s
from utils.fsm import GameState
from utils.dataclasses_ import Position


class UI:
    def __init__(self) -> None:
        self.text_color = (200, 200, 200)
        self.next_text = Text("next", self.text_color, 20, Position(290, 20))
        self.lines_cleared_block = UIBlock(Position(290, 120))
        self.lines_cleared_block.add(
            Text("cleared", self.text_color, 20, Position(0, 0))
        )
        self.lines_cleared_block.add(Text("0", self.text_color, 20, Position(0, 0)))
        self.score_block = UIBlock(Position(290, 180))
        self.score_block.add(Text("score", self.text_color, 20, Position(0, 0)))
        self.score_block.add(Text("0", self.text_color, 20, Position(0, 0)))
        self.level_block = UIBlock(Position(290, 240))
        self.level_block.add(Text("level", self.text_color, 20, Position(0, 0)))
        self.level_block.add(Text("0", self.text_color, 20, Position(0, 0)))

        self.pause = Text(
            "PAUSE", (255, 255, 255), 20, Position(s.GAME_W // 2, s.GAME_H // 2)
        )
        self.game_over = Text(
            "GAME OVER", (255, 255, 255), 20, Position(s.GAME_W // 2, s.GAME_H // 2)
        )

        self.score_plate = NameInput()

        self.fps = Text("fps: 60", self.text_color, 20, Position(290, 400))

    def draw(self, state: GameState) -> None:
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
        self.fps.draw()

    def update_fps(self, fps: str) -> None:
        self.fps.text = "fps: " + fps


interface = UI()
