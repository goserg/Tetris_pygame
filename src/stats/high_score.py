import pickle
import os.path

_save_dir = "../saves/"
_file_name = "high_scores.ttr"


class _HighScore:
    def __init__(self):
        self.score_list = [["", 0] for _ in range(10)]

    def add_score(self, name, score):
        """

        :param name: str
        :param score: int
        :return: 1 if score table has changed, else 0
        """
        if score <= self.score_list[-1][1]:
            return 0
        self.score_list.append([name, score])
        self.score_list = sorted(self.score_list, key=lambda i: i[1], reverse=True)[:-1]
        _save_file()
        return 1

    def is_enough(self, score):
        """

        :param score: int
        :return: True is score is high enough
        """
        if score > self.score_list[-1][1]:
            return True


def _save_file():
    with open(_save_dir+_file_name, "wb") as fw:
        pickle.dump(table, fw)


if not os.path.isfile(_save_dir+_file_name):
    if not os.path.exists(_save_dir):
        os.makedirs(_save_dir)
    table = _HighScore()
else:
    with open(_save_dir+_file_name, "rb") as fr:
        table = pickle.load(fr)
