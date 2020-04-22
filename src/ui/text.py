from ui.text_drawer import display_text
from utils.dataclasses_ import Position


class Text:
    def __init__(self, text: str, color: tuple, size: int, position: Position) -> None:
        self.text = text
        self.size = size
        self.position = position
        self.color = color

    def draw(self) -> None:
        display_text(self.text, self.color, self.size, self.position)
