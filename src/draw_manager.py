import pygame
from utils.window_manager import window
import data.settings as s

bottom_colors = {}
top_colors = {}
side_colors = {}


def compute_colors(colors):
    global bottom_colors
    global top_colors
    global side_colors
    for name, value in colors.items():
        top_colors[name] = _color_brighter(value, 0.7)
        bottom_colors[name] = _color_darker(value, 0.6)
        side_colors[name] = _color_darker(value, 0.9)


def _color_darker(i: tuple, percent: float) -> tuple:
    r = i[0] * percent
    g = i[1] * percent
    b = i[2] * percent
    return r, g, b


def _color_brighter(i: tuple, percent: float) -> tuple:
    r = i[0] + (256 - i[0]) * percent
    g = i[1] + (256 - i[1]) * percent
    b = i[2] + (256 - i[2]) * percent
    return r, g, b


def shade(x, y) -> None:
    x = x * s.scale
    y = y * s.scale
    size = s.CELL_SIZE * s.scale
    pygame.draw.rect(window, s.color_scheme["Shade"], (x, y, size, size))


def cube(x, y, color_tag) -> None:
    x = x * s.scale
    y = y * s.scale
    size = s.CELL_SIZE * s.scale
    pygame.draw.rect(window, s.color_scheme[color_tag], (x, y, size, size))

    if not s.flat_graphics_enabled:
        pygame.draw.polygon(
            window,
            top_colors[color_tag],
            (
                (x, y),
                (x + size, y),
                (x + size * 7 / 8, y + size / 8),
                (x + size / 8, y + size / 8),
            ),
        )
        pygame.draw.polygon(
            window,
            bottom_colors[color_tag],
            (
                (x, y + size),
                (x + size, y + size),
                (x + size * 7 / 8, y + size * 7 / 8),
                (x + size / 8, y + size * 7 / 8),
            ),
        )
        pygame.draw.polygon(
            window,
            side_colors[color_tag],
            (
                (x, y),
                (x, y + size),
                (x + size / 8, y + size * 7 / 8),
                (x + size / 8, y + size / 8),
            ),
        )
        pygame.draw.polygon(
            window,
            side_colors[color_tag],
            (
                (x + size, y),
                (x + size, y + size),
                (x + size * 7 / 8, y + size * 7 / 8),
                (x + size * 7 / 8, y + size / 8),
            ),
        )

    pygame.draw.lines(
        window,
        s.color_scheme["Grid"],
        True,
        [(x, y), (x + size, y), (x + size, y + size), (x, y + size)],
    )
