import utils.settings as s
import utils.controller as controller
from utils.window_manager import window
from grid import Grid
from border import Border
import level
import pygame
from utils.gamepad_controller import GamepadController
import shade
import next_indicator

pygame.init()

grid = Grid()
border = Border()
player = type(next_indicator.next_one)()


def new_player():
    global player
    player = type(next_indicator.next_one)()
    for i in player.body:
        for j in level.cubes:
            if i.position == j.position:
                player = None  # TODO: looks ugy
                return
    shade.shade = type(player)()
    shade.update_pos(player)
    next_indicator.change()


new_player()

controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()


def draw():
    window.fill((0, 0, 0))

    shade.draw()
    player.draw()
    next_indicator.next_one.draw()

    level.draw()
    if s.grid:
        grid.draw() 

    pygame.display.update()


run = True
to_draw = True
pause = False
fall_timer = 0
move_timer = 0
while run:
    pygame.time.delay(s.main_loop_delay)

    controller.get_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if controller.just_pressed["Start"]:
        if not pause:
            pause = True
        else:
            pause = False
            fall_timer = 0
            move_timer = 0

    if not pause:
        if controller.just_pressed["Left"]:
            player.move(-1)
            move_timer = s.delayed_auto_shift
        elif controller.pressed["Left"] and move_timer < 0:
            player.move(-1)
            move_timer = s.auto_shift
        if controller.just_pressed["Right"]:
            player.move(1)
            move_timer = s.delayed_auto_shift
        elif controller.pressed["Right"] and move_timer < 0:
            player.move(1)
            move_timer = s.auto_shift

        if controller.just_pressed["Rotate"]:
            player.try_rotation()

        if (controller.just_pressed["Down"] or (controller.pressed["Down"] and not controller.down_lock))\
                or fall_timer > s.speed:
            controller.down_lock = False
            fall_timer = 0
            if player.move_down():
                new_player()
                controller.down_lock = True
        if controller.just_pressed["Drop"]:
            fall_timer = 0
            player.drop()
            new_player()
        to_draw = True

    if player is None:
        level.cubes.clear()
        new_player()
        border = Border()
        move_timer = 0
        fall_timer = 0
        print("Game over! \nScore:", level.score, "\npress Start to play")
        pause = True
        level.score = 0

    if player:
        shade.update_pos(player)

    if to_draw:
        draw()
        to_draw = False
    fall_timer += 1
    move_timer -= 1
    if controller.just_pressed["Start"]:
        print("Start")
