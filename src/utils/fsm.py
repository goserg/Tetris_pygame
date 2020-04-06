from enum import Enum, auto


class GameState(Enum):
    PAUSE = auto()
    PLAY = auto()
    GAME_OVER = auto()
