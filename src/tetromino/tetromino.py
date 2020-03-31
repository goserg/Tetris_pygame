import utils.controller as controller
import level


class Tetromino:

    def __init__(self):
        self.body = []
        self.pos = (7, 5)
        self.state = 0

    def move_down(self):
        for i in self.body:
            x = i.position[0]
            y = i.position[1] + 1
            for j in level.cubes:
                if j.position == (x, y):
                    self.transfer_to_level()
                    return 1
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x, y + 1
        self.pos = self.pos[0], self.pos[1] + 1

    def move(self):
        """
        :return:
        0 if no move
        1 if land
        else None
        """
        direction = controller.get_direction()
        if controller.is_start_pressed():  # hard drop
            while self.move_down() != 1:
                pass
            return 1
        if direction == (0, 0):
            return 0
        if direction == (0, -1):
            self.rotate()
            for i in level.cubes:
                for j in self.body:
                    if i.position == j.position:
                        self.rotate_back()
                        return
            return
        if direction == (-1, 0) or direction == (1, 0):
            for i in self.body:
                x = i.position[0]
                x += direction[0]
                y = i.position[1]
                y += direction[1]
                for j in level.cubes:
                    if j.position == (x, y):
                        if direction == (0, 1):
                            self.transfer_to_level()
                            return 1
                        return
            for i in self.body:
                x = i.position[0]
                y = i.position[1]
                i.position = x + direction[0], y + direction[1]
        self.pos = self.pos[0] + direction[0], self.pos[1] + direction[1]
        if direction == (0, 1):
            self.move_down()

    def move_down_2(self):
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            y += 1
            for j in level.cubes:
                if j.position == (x, y):
                    self.transfer_to_level()
                    return 1

    def transfer_to_level(self):
        for cube in self.body:
            level.add(cube)
        level.clear_lines()
        self.__init__()

    def rotate(self):
        if self.state == 0:
            self.state = 1
            self.set_1_rotation()
        elif self.state == 1:
            self.state = 2
            self.set_2_rotation()
        elif self.state == 2:
            self.state = 3
            self.set_3_rotation()
        elif self.state == 3:
            self.state = 0
            self.set_0_rotation()

    def rotate_back(self):
        if self.state == 0:
            self.state = 3
            self.set_3_rotation()
        elif self.state == 1:
            self.state = 0
            self.set_0_rotation()
        elif self.state == 2:
            self.state = 1
            self.set_1_rotation()
        elif self.state == 3:
            self.state = 2
            self.set_2_rotation()

    def set_0_rotation(self):
        pass

    def set_1_rotation(self):
        pass

    def set_2_rotation(self):
        pass

    def set_3_rotation(self):
        pass

    def draw(self):
        for i in self.body:
            i.draw()
