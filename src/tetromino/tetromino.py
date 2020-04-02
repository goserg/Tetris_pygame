import level
import shade


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

    def move(self, direct):
        for i in self.body:
            x = i.position[0]
            x += direct
            y = i.position[1]
            for j in level.cubes:
                if j.position == (x, y):
                    return
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x + direct, y
        self.pos = self.pos[0] + direct, self.pos[1]

    def try_rotation(self):
        self.rotate()
        shade.shade.rotate()
        for i in level.cubes:
            for j in self.body:
                if i.position == j.position:
                    self.rotate_back()
                    shade.shade.rotate_back()
                    return

    def drop(self):
        while self.move_down() != 1:
            pass

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
