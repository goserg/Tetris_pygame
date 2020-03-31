import utils.settings as s
import utils.controller as controller
from utils.window_manager import window
from grid import Grid
from border import Border
import level
import pygame
import tetromino.generator
from utils.gamepad_controller import GamepadController

pygame.init()

grid = Grid()
border = Border()
player = tetromino.generator.get_new()

controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()


def draw():
    window.fill((0, 0, 0))

    player.draw()
    level.draw()
    if s.grid:
        grid.draw()

    pygame.display.update()


run = True
to_draw = True
to_move_down = 0
to_move = 0
while run:
    pygame.time.delay(s.main_loop_delay)

    controller.get_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if to_move > s.move_delay:
        result = player.move()
        if result == 1:
            player = tetromino.generator.get_new()
            to_move = 0
        elif result != 0:
            to_move = 0

    if to_move_down == s.speed:
        to_move_down = 0
        if player.move_down():
            player = tetromino.generator.get_new()
    to_draw = True

    if player is None:
        level.cubes.clear()
        player = tetromino.generator.get_new()
        border = Border()

    if to_draw:
        draw()
        to_draw = False
    to_move_down += 1
    to_move += 1

pygame.quit()
