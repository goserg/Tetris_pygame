from dataclasses import dataclass


@dataclass
class Position:
    __slots__ = ("x", "y")
    x: int
    y: int


@dataclass
class Cube:
    __slots__ = ("color_tag", "position")

    position: Position
    color_tag: str

    def __init__(self, position=Position(0, 0), color_tag="Border") -> None:
        self.position = position
        self.color_tag = color_tag
