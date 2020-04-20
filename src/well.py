import data.settings as s
from utils.dataclasses_ import Cube
import stats.score
from typing import List, Optional
import t_draw


well: List[List[Optional[str]]] = [
    [None for _ in range(s.COLUMNS)] for _ in range(s.ROWS)
]
border: List[Cube] = []
lines_cleared = 0


def add(c: Cube) -> None:
    well[int(c.position.y)][int(c.position.x) - 1] = c.color_tag


def clear() -> None:
    global well
    well = [[None for _ in range(s.COLUMNS)] for _ in range(s.ROWS)]


def draw() -> None:
    for i in border:
        t_draw.cube(i.position.x * s.CELL_SIZE, i.position.y * s.CELL_SIZE, i.color_tag)
    for i, col in enumerate(well):
        for j, cube in enumerate(col):
            if cube:
                t_draw.cube((j + 1) * s.CELL_SIZE, i * s.CELL_SIZE, cube)


def clear_lines() -> None:
    lines = 0
    for i, row in enumerate(well):
        if None not in row:
            well.pop(i)
            well.insert(0, [None for _ in range(s.COLUMNS)])
            lines += 1
    stats.score.add(lines)
