import settings.settings as s
import utils.controller as controller
from utils.window_manager import window
from grid import Grid
from border import Border
import well
import pygame
from utils.gamepad_controller import GamepadController
import shade
import next_indicator
from ui.ui import ui
import stats.score
import stats.level
from utils.fsm import GameState
from ui.menu import Menu
from stats.high_score import table as score_list
import datetime

pygame.init()

grid = Grid()
border = Border()
player = type(next_indicator.next_one)()
state = GameState.MENU

menu = Menu()


def game_over():
    global border
    global state
    well.cubes.clear()
    border = Border()
    stats.score.clear()
    well.lines_cleared = 0
    ui.lines_cleared_block.lst[1].text = "0"
    ui.score_block.lst[1].text = "0"
    s.speed = 48


def new_game():
    global move_timer
    global fall_timer
    new_player()
    move_timer = 0
    fall_timer = 0


def new_player():
    global player
    global state
    player = type(next_indicator.next_one)()
    for i in player.body:
        for j in well.cubes:
            if i.position == j.position:
                if score_list.is_enough(stats.score.score):
                    state = GameState.GAME_OVER_RECORD
                else:
                    state = GameState.GAME_OVER
                return
    shade.shade = type(player)()
    shade.update_pos(player)
    next_indicator.change()


controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()

clock = pygame.time.Clock()


def draw():
    global state
    window.fill(s.colors["Background"])
    if state == GameState.PLAY or state == GameState.PAUSE or \
            state == GameState.GAME_OVER_RECORD or state == GameState.GAME_OVER:
        shade.draw()
        player.draw()
        next_indicator.next_one.draw()
        well.draw()
        ui.draw(state)
    if state == GameState.MENU:
        menu.draw()
    if s.grid:
        grid.draw() 

    pygame.display.update()


run = True
to_draw = True
new_game()
while run:
    controller.get_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if controller.just_pressed["Start"]:
        to_draw = True
        if state == GameState.GAME_OVER:
            state = GameState.MENU
            next_indicator.change()
            game_over()
            new_game()
            continue
        elif state == GameState.GAME_OVER_RECORD:
            if score_list.is_enough(stats.score.score):
                if score_list.add_score(ui.score_plate.get_name(), stats.score.score) == 1:
                    menu.update_score()
            state = GameState.MENU
            next_indicator.change()
            game_over()
            new_game()
            continue
        elif state == GameState.PLAY:
            state = GameState.PAUSE
        elif state == GameState.PAUSE:
            state = GameState.PLAY
            fall_timer = 0
            move_timer = 0
    if state == GameState.GAME_OVER_RECORD:
        if ui.score_plate.move(controller.get_direction()) != 0:
            to_draw = True
        if controller.just_pressed["Rotate"]:
            ui.score_plate.add_letter()
            to_draw = True
        elif controller.just_pressed["Clear"]:
            ui.score_plate.clear_name()
            to_draw = True
    elif state == GameState.MENU:
        if menu.change_state():
            to_draw = True
        if controller.just_pressed["Start"]:
            if menu.btn == menu.ButtonPos.START:
                state = GameState.PLAY
                fall_timer = 0
                move_timer = 0
            elif menu.btn == menu.ButtonPos.QUIT:
                run = False

    if state == GameState.PLAY:
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
