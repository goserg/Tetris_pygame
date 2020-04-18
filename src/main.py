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
from ui.menu.menu import Menu
from ui.menu.start_menu import StartMenu
from stats.high_score import table as score_list
from time import time


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
        self.border = Border()
        self.menu = Menu()
        self.start_menu = StartMenu()

        self.clock = pygame.time.Clock()
        self.running = True
        self.to_draw = True

        self.player = type(next_indicator.next_one)()
        shade.shade = type(self.player)()
        shade.update_pos(self.player)
        next_indicator.change()

        self.fps = 0

    def reset_game(self) -> None:
        well.cubes.clear()
        self.border = Border()
        stats.score.clear()
        well.lines_cleared = 0
        ui.lines_cleared_block.lst[1].text = "0"
        ui.score_block.lst[1].text = "0"
        s.speed = 48

    def create_new_player(self) -> None:
        self.player = type(next_indicator.next_one)()
        shade.shade = type(self.player)()
        shade.update_pos(self.player)
        next_indicator.change()

    def draw(self) -> None:
        if self.to_draw:
            self.to_draw = False
            window.fill(s.colors["Background"])
            if (
                self.state == GameState.PLAY
                or self.state == GameState.PAUSE
                or self.state == GameState.GAME_OVER
            ):
                shade.draw()
                self.player.draw()
                next_indicator.next_one.draw()
                well.draw()
                ui.draw(self.state)
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
            self.clock.tick(s.fps_cap)
            self.fps = int(1/(time() - start))

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
            self.reset_game()
            next_indicator.change()
            self.create_new_player()

    def update_play_screen(self) -> None:
        ui.update_fps(str(self.fps))
        if controller.just_pressed["Pause"]:
            self.to_draw = True
            self.state = GameState.PAUSE
        p_event = self.player.update()
        if p_event == 1:  # Player moved
            self.to_draw = True
        elif p_event == 2:  # Player landed
            self.to_draw = True
            self.create_new_player()
            if self.is_game_over():
                self.state = GameState.GAME_OVER
                self.save_score()
                return
        if self.player and p_event:
            shade.update_pos(self.player)

    def update_pause_screen(self) -> None:
        if controller.just_pressed["Pause"]:
            self.to_draw = True
            self.state = GameState.PLAY

    def is_game_over(self) -> bool:
        for i in self.player.body:
            for j in well.cubes:
                if i.position == j.position:
                    return True

    def save_score(self):
        if score_list.is_enough(stats.score.score):
            score_list.add_score(stats.score.player_name, stats.score.score)
            self.menu.update_score()


pygame.init()
controller.gamepad = GamepadController()
controller.keys = pygame.key.get_pressed()

game = Game()
game.run()
pygame.quit()
