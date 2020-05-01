from time import time

import pygame

import data.settings as s
import utils.window_manager
import utils.controller as controller
import utils.args_parser
from utils.fsm import GameState
from utils.gamepad_controller import GamepadController
from ui.interface_manager import interface
from ui.menu.menu import Menu
from ui.menu.start_menu import StartMenu
from grid import Grid
from border import Border
import well
import shade
import next_indicator
import stats


def reset_game() -> None:
    well.clear()
    stats.score.clear()
    well.lines_cleared = 0
    interface.lines_cleared_block.lst[1].text = "0"
    interface.score_block.lst[1].text = "0"
    s.speed = 48


class Game:
    def __init__(self) -> None:
        self.update_action_depending_on_state = {
            GameState.PLAY: self.update_play_screen,
            GameState.MENU: self.update_menu_screen,
            GameState.PAUSE: self.update_pause_screen,
            GameState.GAME_OVER: self.update_game_over_screen,
        }
        self.state = GameState.MENU

        self.grid = Grid()
        self.menu = Menu()
        self.start_menu = StartMenu()
        self.border = Border()

        self.clock = pygame.time.Clock()
        self.running = True
        self.to_draw = True

        self.player = type(next_indicator.next_one)()
        self.create_new_player()

        self.fps = 0

    def create_new_player(self) -> None:
        self.player = type(next_indicator.next_one)()
        if s.is_shade_enabled:
            shade.shade = type(self.player)()
            shade.update_pos(self.player)
        next_indicator.change()

    def draw(self) -> None:
        if self.to_draw:
            self.to_draw = False
            utils.window_manager.window.fill(s.color_scheme["Background"])
            if (
                self.state == GameState.PLAY
                or self.state == GameState.PAUSE
                or self.state == GameState.GAME_OVER
            ):
                if s.is_shade_enabled:
                    shade.draw()
                self.player.draw()
                self.border.draw()
                next_indicator.draw()
                well.draw()
                interface.draw(self.state)
                if s.grid_enabled:
                    self.grid.draw()
            elif self.state == GameState.MENU:
                self.menu.draw()
            elif self.state == GameState.START_MENU:
                self.start_menu.draw()
            pygame.display.update()

    def run(self) -> None:
        while self.running:
            start = time()
            controller.get_keys()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

            self.update_action_depending_on_state[self.state]()

            self.draw()
            self.clock.tick(s.FPS_CAP)
            self.fps = int(1 / (time() - start))

    def update_menu_screen(self) -> None:
        status = self.menu.update()

        if status == 9:
            self.running = False
        elif status == 2:
            self.state = GameState.PLAY
            self.player.reset_timers()
            self.to_draw = True
        elif status:
            self.to_draw = True

    def update_game_over_screen(self) -> None:
        if controller.just_pressed["Start"] or controller.just_pressed["Pause"]:
            self.to_draw = True
            self.state = GameState.MENU
            reset_game()
            next_indicator.change()
            self.create_new_player()

    def update_play_screen(self) -> None:
        interface.update_fps(str(self.fps))
        if controller.just_pressed["Pause"]:
            self.to_draw = True
            self.state = GameState.PAUSE
        self.player.update()
        if self.player.moved:
            if s.is_shade_enabled:
                shade.update_pos(self.player)
            self.to_draw = True
        if self.player.landed:
            self.create_new_player()
            if self.is_game_over():
                self.state = GameState.GAME_OVER
                self.save_score()

    def update_pause_screen(self) -> None:
        if controller.just_pressed["Pause"]:
            self.to_draw = True
            self.state = GameState.PLAY

    def is_game_over(self) -> bool:
        for i in self.player.body:
            cell_x = i.position.x // s.CELL_SIZE
            cell_y = i.position.y // s.CELL_SIZE
            if well.cubes_in_well[cell_y][cell_x - 1]:
                return True
        return False

    def save_score(self):
        if stats.high_score.score_list.is_enough(stats.score.score):
            stats.high_score.score_list.add_score(
                stats.score.player_name, stats.score.score
            )
            self.menu.update_score()


parser = utils.args_parser.ArgsParser()
pygame.init()
controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()

game = Game()
game.run()
pygame.quit()
