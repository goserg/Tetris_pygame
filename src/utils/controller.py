import pygame
from utils.gamepad_controller import GamepadController

keys = []
gamepad: GamepadController

pressed = {
    "Start": False,
    "Pause": False,
    "Back": False,
    "Rotate": False,
    "Left": False,
    "Right": False,
    "Up": False,
    "Down": False,
    "Drop": False,
    "Clear": False,
}

just_pressed = {}

down_lock = False


def get_keys() -> None:
    global pressed
    global just_pressed
    global keys
    just_pressed = {
        "Start": False,
        "Pause": False,
        "Back": False,
        "Rotate": False,
        "Left": False,
        "Right": False,
        "Up": False,
        "Down": False,
        "Drop": False,
        "Clear": False,
    }
    keys = pygame.key.get_pressed()
    joy_direct = gamepad.get_hat()
    # Start the game
    if keys[pygame.K_RETURN] or gamepad.is_A_pressed():
        if not pressed["Start"]:
            just_pressed["Start"] = True
        pressed["Start"] = True
    else:
        pressed["Start"] = False

    # Pause the game
    if keys[pygame.K_ESCAPE] or gamepad.is_start_pressed():
        if not pressed["Pause"]:
            just_pressed["Pause"] = True
        pressed["Pause"] = True
    else:
        pressed["Pause"] = False

    # Back button
    if keys[pygame.K_ESCAPE] or gamepad.is_B_pressed():
        if not pressed["Back"]:
            just_pressed["Back"] = True
        pressed["Back"] = True
    else:
        pressed["Back"] = False

    # Rotate clockwise
    if keys[pygame.K_UP] or keys[pygame.K_x] or gamepad.is_A_pressed():
        if not pressed["Rotate"]:
            just_pressed["Rotate"] = True
        pressed["Rotate"] = True
    else:
        pressed["Rotate"] = False

    # Move left
    if keys[pygame.K_LEFT] or joy_direct[0] == -1:
        if not pressed["Left"]:
            just_pressed["Left"] = True
        pressed["Left"] = True
    else:
        pressed["Left"] = False

    # Move right
    if keys[pygame.K_RIGHT] or joy_direct[0] == 1:
        if not pressed["Right"]:
            just_pressed["Right"] = True
        pressed["Right"] = True
    else:
        pressed["Right"] = False

    # Move down
    if keys[pygame.K_DOWN] or joy_direct[1] == -1:
        if not pressed["Down"]:
            just_pressed["Down"] = True
        pressed["Down"] = True
    else:
        pressed["Down"] = False

    # Move up
    if keys[pygame.K_UP] or joy_direct[1] == 1:
        if not pressed["Up"]:
            just_pressed["Up"] = True
        pressed["Up"] = True
    else:
        pressed["Up"] = False

    # Hard drop
    if keys[pygame.K_SPACE] or joy_direct[1] == 1:
        if not pressed["Drop"]:
            just_pressed["Drop"] = True
        pressed["Drop"] = True
    else:
        pressed["Drop"] = False

    # Clear
    if keys[pygame.K_BACKSPACE] or gamepad.is_B_pressed():
        if not pressed["Clear"]:
            just_pressed["Clear"] = True
        pressed["Clear"] = True
    else:
        pressed["Clear"] = False


def get_direction() -> tuple:
    joy_direct = gamepad.get_hat()
    if keys[pygame.K_DOWN] or joy_direct == (0, 1):
        return 0, 1
    elif keys[pygame.K_UP] or joy_direct == (0, -1):
        return 0, -1
    elif keys[pygame.K_RIGHT] or joy_direct == (1, 0):
        return 1, 0
    elif keys[pygame.K_LEFT] or joy_direct == (-1, 0):
        return -1, 0
    else:
        return 0, 0


def is_Y_pressed():
    return gamepad.is_Y_pressed()
