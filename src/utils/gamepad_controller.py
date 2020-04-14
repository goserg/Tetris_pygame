import pygame


class GamepadController:
    def __init__(self):
        if pygame.joystick.get_count() > 0:
            self.enabled = True
            self.joystick = pygame.joystick.Joystick(0)
            print("{} enabled".format(self.joystick.get_name()))
            self.joystick.init()
            self.pause = 0
        else:
            self.enabled = False

    def get_hat(self):
        if self.enabled:
            return self.joystick.get_hat(0)
        return 0, 0

    def is_start_pressed(self):
        if self.enabled:
            return self.joystick.get_button(7)

    def is_B_pressed(self):
        if self.enabled:
            return self.joystick.get_button(1)

    def is_Y_pressed(self):
        if self.enabled:
            return self.joystick.get_button(3)

    def is_A_pressed(self):
        if self.enabled:
            return self.joystick.get_button(0)
