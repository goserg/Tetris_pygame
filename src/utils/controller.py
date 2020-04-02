import pygame

keys = None
gamepad = None

pressed = {"Start": False,
           "Rotate": False,
           "Left": False,
           "Right": False,
           "Down": False,
           "Drop": False}

just_pressed = {}

down_lock = False


def get_keys():
    global pressed
    global just_pressed
    global keys
    just_pressed = {"Start": False,
                    "Rotate": False,
                    "Left": False,
                    "Right": False,
                    "Down": False,
                    "Drop": False}
    keys = pygame.key.get_pressed()
    joy_direct = gamepad.get_hat()
    if keys[pygame.K_ESCAPE] or gamepad.is_pause_pressed():
        if not pressed["Start"]:
            just_pressed["Start"] = True
        pressed["Start"] = True
    else:
        pressed["Start"] = False
    if keys[pygame.K_UP] or gamepad.is_B_pressed():
        if not pressed["Rotate"]:
            just_pressed["Rotate"] = True
        pressed["Rotate"] = True
    else:
        pressed["Rotate"] = False
    if keys[pygame.K_LEFT] or joy_direct[0] == -1:
        if not pressed["Left"]:
            just_pressed["Left"] = True
        pressed["Left"] = True
    else:
        pressed["Left"] = False
    if keys[pygame.K_RIGHT] or joy_direct[0] == 1:
        if not pressed["Right"]:
            just_pressed["Right"] = True
        pressed["Right"] = True
    else:
        pressed["Right"] = False
    if keys[pygame.K_DOWN] or joy_direct[1] == -1:
        if not pressed["Down"]:
            just_pressed["Down"] = True
        pressed["Down"] = True
    else:
        pressed["Down"] = False
    if keys[pygame.K_SPACE] or gamepad.is_A_pressed():
        if not pressed["Drop"]:
            just_pressed["Drop"] = True
        pressed["Drop"] = True
    else:
        pressed["Drop"] = False


def is_start_pressed():
    if keys[pygame.K_SPACE] or gamepad.is_start_pressed():
        return True


def get_direction():
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
