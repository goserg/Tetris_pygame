import well
import shade
from cube import Cube
import settings.settings as s
import utils.controller as controller


class Tetromino:

    def __init__(self):
        self.body = []
        self.pos = (5, 0)
        self.state = 0
        self.one = Cube(tag="Block")
        self.two = Cube(tag="Block")
        self.three = Cube(tag="Block")
        self.four = Cube(tag="Block")
        self.body.append(self.one)
        self.body.append(self.two)
        self.body.append(self.three)
        self.body.append(self.four)

        self.move_timer = 0
        self.fall_timer = 0

    def update(self):
        """

        :return: 0 if nothing happened
        :return: 1 if moved
        :return: 2 if landed
        """
        to_draw = 0
        if controller.just_pressed["Left"]:
            if self.move(-1) == 1:
                to_draw = 1
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Left"] and self.move_timer < 0:
            if self.move(-1) == 1:
                to_draw = 1
            self.move_timer = s.auto_shift
        if controller.just_pressed["Right"]:
            if self.move(1) == 1:
                to_draw = 1
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Right"] and self.move_timer < 0:
            if self.move(1) == 1:
                to_draw = 1
            self.move_timer = s.auto_shift

        if controller.just_pressed["Rotate"]:
            if self.try_rotation():
                to_draw = 1
            elif s.wall_push and self.move(1) == 1 and self.try_rotation():
                to_draw = 1
            elif s.wall_push and self.move(-1) == 1 and self.try_rotation():
                to_draw = 1
            elif s.wall_push and self.body[0].color_tag == "TypeI" and self.move(1) == 1 and self.move(1) == 1 and self.try_rotation():
                to_draw = 1
            elif s.wall_push and self.body[0].color_tag == "TypeI" and self.move(-1) == 1 and self.move(-1) == 1 and self.try_rotation():
                to_draw = 1

        if (controller.just_pressed["Down"] or (controller.pressed["Down"] and not controller.down_lock))\
                or self.fall_timer > s.speed:
            controller.down_lock = False
            self.fall_timer = 0
            if self.move_down() == 1:
                controller.down_lock = True
                return 2
            to_draw = 1
        if s.drop_enabled and controller.just_pressed["Drop"]:
            self.fall_timer = 0
            self.drop()
            return 2
        self.move_timer -= 1
        self.fall_timer += 1
        return to_draw

    def reset_timers(self):
        self.move_timer = 0
        self.fall_timer = 0

    def move_down(self):
        """

        :return:  1 if landed, 2 if moved
        """
        for i in self.body:
            x = i.position[0]
            y = i.position[1] + 1
            for j in well.cubes:
                if j.position == (x, y):
                    self.transfer_to_level()
                    return 1
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x, y + 1
        self.pos = self.pos[0], self.pos[1] + 1
        return 2

    def move(self, direct):
        """

        :param direct: 1 if move right, -1 if move left
        :return: 0 if can't move, 1 if moved
        """
        for i in self.body:
            x = i.position[0]
            x += direct
            y = i.position[1]
            for j in well.cubes:
                if j.position == (x, y):
                    return 0
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x + direct, y
        self.pos = self.pos[0] + direct, self.pos[1]
        return 1

    def try_rotation(self):
        """

        :return: 0 if can't rotate, 1 if rotated
        """
        self.rotate()
        shade.shade.rotate()
        for i in well.cubes:
            for j in self.body:
                if i.position == j.position:
                    self.rotate_back()
                    shade.shade.rotate_back()
                    return 0
        return 1

    def drop(self):
        while self.move_down() != 1:
            pass

    def transfer_to_level(self):
        for cube in self.body:
            well.add(cube)
        well.clear_lines()
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
