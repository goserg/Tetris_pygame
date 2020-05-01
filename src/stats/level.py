import data.settings as s
import data.colors
import ui.interface_manager
import draw_manager

LEVEL_SPEEDS = [
    48,
    43,
    38,
    33,
    28,
    23,
    18,
    13,
    8,
    6,
    5,
    5,
    5,
    4,
    4,
    4,
    3,
    3,
    3,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
]

level = 0


def reset() -> None:
    global level
    level = 0
    s.speed = LEVEL_SPEEDS[level]
    ui.interface_manager.interface.level_block.lst[1].text = str(level)
    s.color_scheme = data.colors.level_1
    draw_manager.compute_colors(s.color_scheme)


def set_level(lines: int) -> None:
    global level
    if level > lines // 10:
        return
    level = lines // 10
    if level < len(LEVEL_SPEEDS):
        s.speed = LEVEL_SPEEDS[level]
    else:
        s.speed = LEVEL_SPEEDS[-1]
    if not s.standard_colors:
        color_scheme_update()
    draw_manager.compute_colors(s.color_scheme)
    ui.interface_manager.interface.level_block.lst[1].text = str(level)


def color_scheme_update() -> None:
    n = level % 4
    if n == 0:
        s.color_scheme = data.colors.level_1
    elif n == 1:
        s.color_scheme = data.colors.level_2
    elif n == 2:
        s.color_scheme = data.colors.level_3
    else:
        s.color_scheme = data.colors.level_4
