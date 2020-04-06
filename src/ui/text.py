from ui.text_drawer import display_text


class Text:
    def __init__(self, text, color, size, x, y):
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        display_text(self.text, self.color, self.size, self.x, self.y)
