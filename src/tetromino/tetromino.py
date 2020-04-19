import well
import shade
from cube import Cube
import settings.settings as s
import utils.controller as controller
from utils.dataclasses_ import Position


class Tetromino:
    def __init__(self) -> None:
        self.body = []
        self.position = Position(5, 0)
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

        self.moved = False
        self.landed = False

    def update(self) -> None:
        self.moved = False
        if controller.just_pressed["Left"]:
            if self.can_slide(-1):
                self.slide(-1)
                self.moved = True
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Left"] and self.move_timer < 0:
            if self.can_slide(-1):
                self.slide(-1)
                self.moved = True
            self.move_timer = s.auto_shift
        if controller.just_pressed["Right"]:
            if self.can_slide(1):
                self.slide(1)
                self.moved = True
            self.move_timer = s.delayed_auto_shift
        elif controller.pressed["Right"] and self.move_timer < 0:
            if self.can_slide(1):
                self.slide(1)
                self.moved = True
            self.move_timer = s.auto_shift

        if controller.just_pressed["Rotate"]:
            if self.try_rotation():
                self.moved = True
            elif s.is_wall_push_enabled:
                if self.wall_push_rotation():
                    self.moved = True
        if (
            controller.just_pressed["Down"]
            or (controller.pressed["Down"] and not controller.down_lock)
        ) or self.fall_timer > s.speed:
            self.moved = True
            if not self.can_move_down():
                self.transfer_to_level()
                well.clear_lines()
                controller.down_lock = True
                self.landed = True
                return
            self.move_down()
            controller.down_lock = False
            self.fall_timer = 0
        elif s.drop_enabled and controller.just_pressed["Drop"]:
            self.fall_timer = 0
            self.drop()
            self.landed = True
            self.moved = True
            return
        self.move_timer -= 1
        self.fall_timer += 1

    def wall_push_rotation(self) -> bool:
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

    def can_move_down(self) -> bool:
        for i in self.body:
            x = i.position.x
            y = i.position.y + 1
            for j in well.cubes:
                if j.position.x == x and j.position.y == y:
                    return False
        return True

    def move_down(self) -> None:
        for i in self.body:
            y = i.position.y
            i.position.y = y + 1
        self.position.y += 1

    def can_slide(self, direct: int) -> bool:
        for i in self.body:
            x = i.position.x + direct
            y = i.position.y
            for j in well.cubes:
                if j.position.x == x and j.position.y == y:
                    return False
        return True

    def slide(self, direct: int) -> None:
        """
        :param direct: positive if move right, negative if move left
        """
        for i in self.body:
            i.position.x += direct
        self.position.x += direct

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
        while self.can_move_down():
            self.move_down()

    def transfer_to_level(self) -> None:
        for cube in self.body:
            well.add(cube)

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
