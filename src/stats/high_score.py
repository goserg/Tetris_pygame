import pickle
import os.path

_save_dir = "../saves/"
_file_name = "high_scores.ttr"


class _HighScore:
    def __init__(self) -> None:
        self.score_list = [["", 0] for _ in range(10)]
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4"]

    def change_name(self, name: str, i: int) -> None:
        self.players[i] = name
        _save_file()

    def add_score(self, name: str, score: int) -> int:
        """
        :return: 1 if score table has changed, else 0
        """
        if score <= self.score_list[-1][1]:
            return 0
        self.score_list.append([name, score])
        self.score_list = sorted(self.score_list, key=lambda i: i[1], reverse=True)[:-1]
        _save_file()
        return 1

    def is_enough(self, score: int) -> bool:
        """
        :return: True is score is high enough
        """
        if score > self.score_list[-1][1]:
            return True


def _save_file() -> None:
    with open(_save_dir + _file_name, "wb") as fw:
        pickle.dump(score_list, fw)
    print("save file changed")


if not os.path.isfile(_save_dir + _file_name):
    if not os.path.exists(_save_dir):
        os.makedirs(_save_dir)
    score_list = _HighScore()
else:
    with open(_save_dir + _file_name, "rb") as fr:
        score_list = pickle.load(fr)
