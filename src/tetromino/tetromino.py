import utils.controller as controller
import level
from cube import Cube


class Tetromino:
    head = None

    def __init__(self):
        self.body = []
        self.head = Cube((7, 2), (0, 150, 0))
        self.body.append(self.head)

    def move_down(self):
        for i in self.body:
            x = i.position[0]
            y = i.position[1] + 1
            for j in level.cubes:
                if j.position == (x, y):
                    for cube in self.body:
                        level.add(cube)
                    self.__init__()
                    return True
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x, y + 1

    def move(self):
        direction = controller.get_direction()
        if direction == (0, 1) or direction == (-1, 0) or direction == (1, 0):
            for i in self.body:
                x = i.position[0]
                x += direction[0]
                y = i.position[1]
                y += direction[1]
                for j in level.cubes:
                    if j.position == (x, y):
                        if direction == (0, 1):
                            for cube in self.body:
                                level.add(cube)
                            self.__init__()
                            return True
                        return

            for i in self.body:
                x = i.position[0]
                y = i.position[1]
                i.position = x + direction[0], y + direction[1]

    def rotate(self):
        pass

    def draw(self):
        for i in self.body:
            i.draw()
