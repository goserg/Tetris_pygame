import settings.settings as s
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


def game_over():
    global border
    level.cubes.clear()
    border = Border()
    print("Game over! \nScore:", level.score, "\npress Start to play")
    level.score = 0
    level.lines_cleared = 0
    s.speed = 48


def new_game():
    global move_timer
    global fall_timer
    global pause
    new_player()
    move_timer = 0
    fall_timer = 0
    pause = True


def new_player():
    global player
    player = type(next_indicator.next_one)()
    for i in player.body:
        for j in level.cubes:
            if i.position == j.position:
                game_over()
                new_game()
                return
    shade.shade = type(player)()
    shade.update_pos(player)
    next_indicator.change()


controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()

clock = pygame.time.Clock()


def draw():
    window.fill(s.colors["Background"])

    shade.draw()
    player.draw()
    next_indicator.next_one.draw()

    level.draw()
    if s.grid:
        grid.draw() 

    pygame.display.update()


run = True
to_draw = True
new_game()
pause = False
while run:
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
            if player.move(-1) == 1:
                to_draw = True
            move_timer = s.delayed_auto_shift
        elif controller.pressed["Left"] and move_timer < 0:
            if player.move(-1) == 1:
                to_draw = True
            move_timer = s.auto_shift
        if controller.just_pressed["Right"]:
            if player.move(1) == 1:
                to_draw = True
            move_timer = s.delayed_auto_shift
        elif controller.pressed["Right"] and move_timer < 0:
            if player.move(1) == 1:
                to_draw = True
            move_timer = s.auto_shift

        if controller.just_pressed["Rotate"]:
            if player.try_rotation():
                to_draw = True

        if (controller.just_pressed["Down"] or (controller.pressed["Down"] and not controller.down_lock))\
                or fall_timer > s.speed:
            controller.down_lock = False
            fall_timer = 0
            if player.move_down() == 1:
                new_player()
                controller.down_lock = True
            to_draw = True
        if s.drop_enabled and controller.just_pressed["Drop"]:
            fall_timer = 0
            player.drop()
            new_player()
            to_draw = True

    if player:
        shade.update_pos(player)

    if to_draw:
        draw()
        to_draw = False
    fall_timer += 1
    move_timer -= 1
    clock.tick(s.fps_cap)

pygame.quit()
