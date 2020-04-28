import argparse
import data.settings as s
import utils.window_manager


class ArgsParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-sc',
            '--scale',
            type=float,
            default=2,
            help='scale of the game window (default: %(default)s)',
            metavar='',
        )
        parser.add_argument(
            '-f',
            '--flat',
            default="False",
            choices=['True', 'False'],
            help='toggling 3D-ish graphics off (default: %(default)s)',
            metavar='',
        )
        parser.add_argument(
            '-g',
            '--grid',
            default="False",
            choices=['True', 'False'],
            help='toggle grid on (default: %(default)s)',
            metavar='',
        )
        parser.add_argument(
            '-sh',
            '--shade',
            default="True",
            choices=['True', 'False'],
            help='toggle shade on (default: %(default)s)',
            metavar='',
        )
        parser.add_argument(
            '-wp',
            '--wallpush',
            default="True",
            choices=['True', 'False'],
            help='toggle grid on (default: %(default)s)',
            metavar='',
        )
        parser.add_argument(
            '-c',
            '--colors',
            default="False",
            choices=['True', 'False'],
            help='toggle standard tetris style colors on (default: %(default)s)',
            metavar='',
        )
        args = parser.parse_args()
        s.scale = args.scale
        s.flat_graphics_enabled = True if args.flat == "True" else False
        s.grid_enabled = True if args.grid == "True" else False
        s.is_wall_push_enabled = True if args.wallpush == "True" else False
        s.is_shade_enabled = True if args.shade == "True" else False
        s.standard_colors = True if args.colors == "True" else False
        utils.window_manager.resize_window()
