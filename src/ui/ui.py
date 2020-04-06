from ui.text import Text
from ui.ui_block import UIBlock


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

    def draw(self):
        self.next_text.draw()
        self.lines_cleared_block.draw()
        self.score_block.draw()
        self.level_block.draw()


ui = UI()
