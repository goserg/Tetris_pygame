from ui.text_drawer import display_text


class Text:
    def __init__(self, text: str, color: tuple, size: int, x: int, y: int) -> None:
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self) -> None:
        display_text(self.text, self.color, self.size, self.x, self.y)
