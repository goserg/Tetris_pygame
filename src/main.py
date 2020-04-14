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
from ui.start_menu import StartMenu
from stats.high_score import table as score_list

pygame.init()

grid = Grid()
border = Border()
player = type(next_indicator.next_one)()
state = GameState.MENU

menu = Menu()
start_menu = StartMenu()


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


def new_player():
    global player
    global state
    player = type(next_indicator.next_one)()
    for i in player.body:
        for j in well.cubes:
            if i.position == j.position:
                state = GameState.GAME_OVER
                if score_list.is_enough(stats.score.score):
                    score_list.add_score(start_menu.player.text, stats.score.score)
                    menu.update_score()
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
            state == GameState.GAME_OVER:
        shade.draw()
        player.draw()
        next_indicator.next_one.draw()
        well.draw()
        ui.draw(state)
    if state == GameState.MENU:
        menu.draw()
    elif state == GameState.START_MENU:
        start_menu.draw()
    if s.grid:
        grid.draw() 

    pygame.display.update()


run = True
to_draw = True
new_player()
while run:
    controller.get_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if state == GameState.MENU:
        if menu.change_state():
            to_draw = True
        if controller.just_pressed["Start"]:
            to_draw = True
            if menu.btn == menu.ButtonPos.PLAY:
                state = GameState.START_MENU
            elif menu.btn == menu.ButtonPos.QUIT:
                run = False
    elif state == GameState.START_MENU:
        status = start_menu.update()

        if status:
            to_draw = True
        if status == 1:
            state = GameState.PLAY
            player.reset_timers()
        elif status == 9:
            state = GameState.MENU

    elif state == GameState.GAME_OVER:
        if controller.just_pressed["Start"] or controller.just_pressed["Pause"]:
            to_draw = True
            state = GameState.MENU
            next_indicator.change()
            game_over()
            new_player()
            continue
    elif state == GameState.PLAY:
        if controller.just_pressed["Pause"]:
            to_draw = True
            state = GameState.PAUSE
        p_event = player.update()
        if p_event == 1:  # Player moved
            to_draw = True
        elif p_event == 2:  # Player landed
            new_player()
            to_draw = True
    elif state == GameState.PAUSE:
        if controller.just_pressed["Pause"]:
            to_draw = True
            state = GameState.PLAY

    if player:
        shade.update_pos(player)

    if to_draw:
        draw()
        to_draw = False
    clock.tick(s.fps_cap)

pygame.quit()
