from enum import Enum, auto


class GameState(Enum):
    PAUSE = auto()
    PLAY = auto()
    GAME_OVER = auto()
    GAME_OVER_RECORD = auto()
    MENU = auto()
    START_MENU = auto()


class MenuState(Enum):
    MAIN = auto()
    START = auto()
    SCORE = auto()
