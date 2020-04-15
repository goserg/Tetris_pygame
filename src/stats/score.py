import stats.level
from ui.ui import ui

score = 0
lines = 0
player_name = "anonymous"


def clear():
    global score
    global lines
    score = 0
    lines = 0
    stats.level.reset()


def add(l):
    global score
    global lines
    if l == 0:
        inc = 0
    elif l == 1:
        inc = 40
    elif l == 2:
        inc = 100
    elif l == 3:
        inc = 300
    else:
        inc = 1200
    score += inc * (stats.level.level + 1)
    lines += l
    ui.score_block.lst[1]._text = str(score)
    ui.lines_cleared_block.lst[1]._text = str(lines)
    stats.level.set_level(lines)
