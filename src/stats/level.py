import settings.settings as s
from ui.ui import ui
level = 0

levels = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]


def reset():
    global level
    level = 0
    s.speed = levels[level]
    ui.level_block.lst[1].text = str(level)


def set_level(lines):
    global level
    level = lines // 10
    if level < len(levels):
        s.speed = levels[level]
    else:
        s.speed = levels[-1]
    ui.level_block.lst[1].text = str(level)
