import well
import shade
from cube import Cube
import settings.settings as s
import utils.controller as controller


class Tetromino:
    def __init__(self) -> None:
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

    def update(self) -> int:
        """
        :returns: 0 if nothing happened; 1 if moved; 2 if landed
        """
        to_draw = 0
        if controller.just_pressed["Left"]:
            if self.can_slide(-1):
                self.slide(-1)
                to_draw = 1
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Left"] and self.move_timer < 0:
            if self.can_slide(-1):
                self.slide(-1)
                to_draw = 1
            self.move_timer = s.auto_shift
        if controller.just_pressed["Right"]:
            if self.can_slide(1):
                self.slide(1)
                to_draw = 1
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Right"] and self.move_timer < 0:
            if self.can_slide(1):
                self.slide(1)
                to_draw = 1
            self.move_timer = s.auto_shift

        if controller.just_pressed["Rotate"]:
            if self.try_rotation():
                to_draw = 1
            elif s.is_wall_push_enabled:
                if self.wall_rotation():
                    to_draw = 1
        if (
            controller.just_pressed["Down"]
            or (controller.pressed["Down"] and not controller.down_lock)
        ) or self.fall_timer > s.speed:
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

    def wall_rotation(self) -> bool:
        self.rotate()
        if self.can_slide(1):
            self.slide(1)
            return True
        elif self.can_slide(-1):
            self.slide(-1)
            return True
        if self.body[0].color_tag == "TypeI":
            if self.can_slide(2):
                self.slide(2)
                return True
            elif self.can_slide(-2):
                self.slide(-2)
                return True
        self.rotate_back()
        return False

    def reset_timers(self) -> None:
        self.move_timer = 0
        self.fall_timer = 0

    def move_down(self) -> int:
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

    def can_slide(self, direct: int) -> bool:
        for i in self.body:
            x = i.position[0]
            x += direct
            y = i.position[1]
            for j in well.cubes:
                if j.position == (x, y):
                    return False
        return True

    def slide(self, direct: int) -> None:
        """
        :param direct: positive if move right, negative if move left
        """
        for i in self.body:
            x = i.position[0]
            y = i.position[1]
            i.position = x + direct, y
        self.pos = self.pos[0] + direct, self.pos[1]

    def try_rotation(self) -> bool:
        """
        :return: False if can't rotate, True if rotated
        """
        self.rotate()
        for i in well.cubes:
            for j in self.body:
                if i.position == j.position:
                    self.rotate_back()
                    return False
        shade.shade.rotate()
        return True

    def drop(self) -> None:
        while self.move_down() != 1:
            pass

    def transfer_to_level(self) -> None:
        for cube in self.body:
            well.add(cube)
        well.clear_lines()
        self.__init__()

    def rotate(self) -> None:
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

    def rotate_back(self) -> None:
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

    def set_0_rotation(self) -> None:
        pass

    def set_1_rotation(self) -> None:
        pass

    def set_2_rotation(self) -> None:
        pass

    def set_3_rotation(self) -> None:
        pass

    def draw(self) -> None:
        for i in self.body:
            i.draw()
