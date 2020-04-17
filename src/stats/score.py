import stats.level
from ui.ui import ui

score = 0
lines = 0
player_name = "anonymous"


def clear() -> None:
    global score
    global lines
    score = 0
    lines = 0
    stats.level.reset()


def add(lns: int) -> None:
    global score
    global lines
    if lns == 0:
        inc = 0
    elif lns == 1:
        inc = 40
    elif lns == 2:
        inc = 100
    elif lns == 3:
        inc = 300
    else:
        inc = 1200
    score += inc * (stats.level.level + 1)
    lines += lns
    ui.score_block.lst[1].text = str(score)
    ui.lines_cleared_block.lst[1].text = str(lines)
    stats.level.set_level(lines)
