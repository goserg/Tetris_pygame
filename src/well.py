import data.settings as s
from utils.dataclasses_ import Cube
import stats.score
from typing import List, Optional
import t_draw


cubes_in_well: List[List[Optional[str]]] = [
    [None for _ in range(s.COLUMNS)] for _ in range(s.ROWS)
]
lines_cleared = 0


def add(c: Cube) -> None:
    cubes_in_well[int(c.position.y // s.CELL_SIZE)][
        int(c.position.x // s.CELL_SIZE) - 1
    ] = c.color_tag


def clear() -> None:
    global cubes_in_well
    cubes_in_well = [[None for _ in range(s.COLUMNS)] for _ in range(s.ROWS)]


def draw() -> None:
    for i, col in enumerate(cubes_in_well):
        for j, cube in enumerate(col):
            if cube:
                t_draw.cube((j + 1) * s.CELL_SIZE, i * s.CELL_SIZE, cube)


def clear_lines() -> None:
    lines = 0
    for i, row in enumerate(cubes_in_well):
        if None not in row:
            cubes_in_well.pop(i)
            cubes_in_well.insert(0, [None for _ in range(s.COLUMNS)])
            lines += 1
    stats.score.add(lines)
