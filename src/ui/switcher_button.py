import utils.controller as controller
from ui.text import Text
from ui.arrow import Arrow


class SwitcherButton:
    """
    text with multiple text values
    switch between values with buttons Left and Right if horizontal == True
    else with buttons Up and Down

    get_text() returns current text
    get_current_index() returns current index
    """

    def __init__(
        self,
        options: list,
        current_index: int,
        color: tuple,
        size: int,
        x: int,
        y: int,
        horizontal: bool = True,
    ) -> None:
        self._options = options
        self._current_index = current_index
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.horizontal = horizontal

        self._text = Text(options[current_index], color, size, x, y)

        if horizontal:
            self.width = int(size * (len(options[current_index])) / 3.3 + 5)
            self.ar1 = Arrow(
                self._text.x - self.width,
                self._text.y,
                size,
                horizontal=True,
                flip=False,
                tag="Left",
            )
            self.ar2 = Arrow(
                self._text.x + self.width,
                self._text.y,
                size,
                horizontal=True,
                flip=True,
                tag="Right",
            )
        else:
            self.ar1 = Arrow(
                self._text.x,
                self._text.y - size,
                size,
                horizontal=False,
                flip=False,
                tag="Up",
            )
            self.ar2 = Arrow(
                self._text.x,
                self._text.y + size,
                size,
                horizontal=False,
                flip=True,
                tag="Down",
            )

    def update(self) -> bool:
        to_redraw = False
        if controller.just_pressed["Right" if self.horizontal else "Up"]:
            self._current_index += 1
            if self._current_index >= len(self._options):
                self._current_index = 0
            self._update_text()
            to_redraw = True
        elif controller.just_pressed["Left" if self.horizontal else "Down"]:
            self._current_index -= 1
            if self._current_index < 0:
                self._current_index = len(self._options) - 1
            self._update_text()
            to_redraw = True
        if self.ar1.update():
            to_redraw = True
        if self.ar2.update():
            to_redraw = True
        return to_redraw

    def _update_text(self) -> None:
        self._text.text = self._options[self._current_index]
        if self.horizontal:
            self.width = self.size * (len(self._options[self._current_index])) / 3.3 + 5
            self.ar1.x = self._text.x - self.width
            self.ar2.x = self._text.x + self.width

    def draw(self) -> None:
        self._text.draw()
        self.ar1.draw()
        self.ar2.draw()

    def get_text(self) -> str:
        return self._text.text

    def get_index(self) -> int:
        return self._current_index

    def set_options(self, options: list) -> None:
        self._options = options
        self._update_text()
