import settings.settings as s
import settings.colors as colors
from ui.ui import ui

LEVELS = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

level = 0


def reset():
    global level
    level = 0
    s.speed = LEVELS[level]
    ui.level_block.lst[1].text = str(level)
    s.colors = colors.level_1


def set_level(lines):
    global level
    if level > lines // 10:
        return
    level = lines // 10
    if level < len(LEVELS):
        s.speed = LEVELS[level]
    else:
        s.speed = LEVELS[-1]
    color_change()
    ui.level_block.lst[1].text = str(level)


def color_change():
    n = level % 4
    if n == 0:
        s.colors = colors.level_1
    elif n == 1:
        s.colors = colors.level_2
    elif n == 2:
        s.colors = colors.level_3
    else:
        s.colors = colors.level_4
