import well
import shade
from utils.dataclasses_ import Cube
import data.settings as s
import utils.controller as controller
from utils.dataclasses_ import Position
import t_draw


class Tetromino:
    __slots__ = ("position", "state", "body", "_move_timer", "_fall_timer", "moved", "landed")

    def __init__(self) -> None:
        self.position = Position(5 * s.CELL_SIZE, 0)
        self.state = 0

        self.body = [Cube() for _ in range(4)]

        self._move_timer = 0
        self._fall_timer = 0

        self.moved = False
        self.landed = False

    def update(self) -> None:
        self.moved = False
        if controller.just_pressed["Left"]:
            if self._can_slide(-1):
                self._slide(-1)
                self.moved = True
            self._move_timer = s.DELAYED_AUTO_SHIFT
        elif controller.pressed["Left"] and self._move_timer < 0:
            if self._can_slide(-1):
                self._slide(-1)
                self.moved = True
            self._move_timer = s.AUTO_SHIFT
        if controller.just_pressed["Right"]:
            if self._can_slide(1):
                self._slide(1)
                self.moved = True
            self._move_timer = s.DELAYED_AUTO_SHIFT
        elif controller.pressed["Right"] and self._move_timer < 0:
            if self._can_slide(1):
                self._slide(1)
                self.moved = True
            self._move_timer = s.AUTO_SHIFT

        if controller.just_pressed["Rotate"]:
            if self._try_rotation():
                self.moved = True
            elif s.is_wall_push_enabled:
                if self._wall_push_rotation():
                    self.moved = True
        if (
            controller.just_pressed["Down"]
            or (controller.pressed["Down"] and not controller.down_lock)
        ) or self._fall_timer > s.speed:
            self.moved = True
            if not self._can_move_down():
                self._transfer_to_level()
                well.clear_lines()
                controller.down_lock = True
                self.landed = True
                return
            self._move_down()
            controller.down_lock = False
            self._fall_timer = 0
        self._move_timer -= 1
        self._fall_timer += 1

    def reset_timers(self) -> None:
        self._move_timer = 0
        self._fall_timer = 0

    def _can_move_down(self) -> bool:
        for i in self.body:
            cell_x = i.position.x // s.CELL_SIZE
            cell_y = i.position.y // s.CELL_SIZE + 1
            if cell_y >= len(well.cubes_in_well) - 1:
                return False
            if well.cubes_in_well[cell_y][cell_x - 1]:
                return False
        return True

    def _move_down(self) -> None:
        for i in self.body:
            i.position.y += s.CELL_SIZE
        self.position.y += s.CELL_SIZE

    def _can_slide(self, direct: int) -> bool:
        for i in self.body:
            cell_x = i.position.x // s.CELL_SIZE + direct
            cell_y = i.position.y // s.CELL_SIZE
            if cell_x <= 0 or cell_x > len(well.cubes_in_well[0]):
                return False
            if well.cubes_in_well[cell_y][cell_x - 1]:
                return False
        return True

    def _slide(self, direct: int) -> None:
        """
        :param direct: positive if move right, negative if move left
        """
        for i in self.body:
            i.position.x += direct * s.CELL_SIZE
        self.position.x += direct * s.CELL_SIZE

    def _try_rotation(self) -> bool:
        """
        :return: False if can't rotate, True if rotated
        """
        self._rotate()
        for i in self.body:
            cell_x = i.position.x // s.CELL_SIZE
            cell_y = i.position.y // s.CELL_SIZE
            if cell_y >= len(well.cubes_in_well) - 1:
                self._rotate_back()
                return False
            if cell_x <= 0 or cell_x > len(well.cubes_in_well[0]):
                self._rotate_back()
                return False
            if well.cubes_in_well[cell_y][cell_x - 1]:
                self._rotate_back()
                return False
        if s.is_shade_enabled:
            shade.shade._rotate()
        return True

    def _wall_push_rotation(self) -> bool:
        self._rotate()
        if self._can_slide(1):
            self._slide(1)
            return True
        elif self._can_slide(-1):
            self._slide(-1)
            return True
        if self.body[0].color_tag == "TypeI":
            if self._can_slide(2):
                self._slide(2)
                return True
            elif self._can_slide(-2):
                self._slide(-2)
                return True
        self._rotate_back()
        return False

    def _drop(self) -> None:
        while self._can_move_down():
            self._move_down()

    def _transfer_to_level(self) -> None:
        for cube in self.body:
            well.add(cube)

    def _rotate(self) -> None:
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

    def _rotate_back(self) -> None:
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
            t_draw.cube(i.position.x, i.position.y, i.color_tag)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position.x}, {self.position.y})"
