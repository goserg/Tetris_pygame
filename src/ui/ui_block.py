from utils.dataclasses_ import Position
from ui.text import Text


class UIBlock:
    def __init__(self, position: Position) -> None:
        self.lst = []
        self.position = position

    def add(self, obj: Text) -> None:
        if not self.lst:
            obj.position.x = self.position.x
            obj.position.y = self.position.y
        else:
            obj.position.x = self.position.x
            obj.position.y = self.lst[-1].position.y + self.lst[-1].size
        self.lst.append(obj)

    def draw(self) -> None:
        for i in self.lst:
            i.draw()
