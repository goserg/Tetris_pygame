from typing import Optional

from dataclasses import dataclass


@dataclass
class Position:
    __slots__ = ("x", "y")
    x: int
    y: int


@dataclass
class Cube:
    __slots__ = ("position", "color_tag")

    position: Optional[Position]
    color_tag: Optional[str]

    def __init__(self, position=None, color_tag=None) -> None:
        self.position = position
        self.color_tag = color_tag
