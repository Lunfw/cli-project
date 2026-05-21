from src.loader import Loader
from src.errors import Logger
from shutil     import get_terminal_size
from typing     import List, Dict
from termios    import tcgetattr, tcsetattr, TCSADRAIN, ICANON, ECHO, IEXTEN, VMIN, VTIME
from sys        import stdin, stdout
from importlib  import util
from os         import path, listdir


class PluginView:
    _current_line: int  = 0

    @staticmethod
    def write(text: str) -> None:
        cols, rows  = get_terminal_size()
        view_top    = 3
        cli_height  = 3
        view_height = rows - 2 - cli_height - view_top
        x           = 5
        max_width   = cols - 8

        if (PluginView._current_line >= view_height - 1):
            return

        y    = view_top + PluginView._current_line
        text = text[:max_width]
        stdout.write(f'\033[{y};{x}H{text}')
        stdout.flush()
        PluginView._current_line += 1

    @staticmethod
    def clear() -> None:
        cols, rows  = get_terminal_size()
        width       = cols - 8
        view_top    = 3
        cli_height  = 3
        view_height = rows - 2 - cli_height - view_top

        for i in range(view_height):
            stdout.write(f'\033[{view_top + i};{4}H' + ' ' * (width - 2))
        PluginView._current_line    = 0
        stdout.flush()

    @staticmethod
    def draw_window() -> None:
        cols, rows  = get_terminal_size()
        width       = cols - 6
        x           = 3

        cli_height  = 3
        view_top    = 2
        view_height = rows - 2 - cli_height - view_top

        top         = '╭' + '─' * width + '╮'
        middle      = '│' + ' ' * width + '│'
        bottom      = '╰' + '─' * width + '╯'

        stdout.write(f'\033[{view_top};{x}H'     + top)
        for i in range(1, view_height):
            stdout.write(f'\033[{view_top + i};{x}H' + middle)
        stdout.write(f'\033[{view_top + view_height};{x}H' + bottom)
        stdout.flush()


class CLIBar:
    @staticmethod
    def _handle_command(cmd: str) -> bool:
        parts               = cmd.strip().split()
        if (not parts):
            return False
        name                = parts[0]
        args                = parts[1:]
        cmd_list: Dict[str] = Loader.load_json('./config.json')[0]['commands']

        cmd_dict: Dict[str] = dict(Loader._load_plugins(cmd_list))

        if (name not in cmd_dict):
            Logger.log('Command not found -> ' + name, 'ERROR')
            return False

        path    = cmd_dict[name]
        spec    = util.spec_from_file_location(name, path)
        module  = util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if (not hasattr(module, 'Plugin')):
            Logger.log('Commands/plugins require Plugin class -> ' + name, 'ERROR')
            return False

        if (not len(args)):
            args    = None

        plugin  = module.Plugin()
        Logger.log(f'Running command: {name}')
        Logger.separate()
        plugin.run(args, PluginView)
        Logger.separate()
        return True

    @staticmethod
    def draw_bar() -> None:
        cols, rows  = get_terminal_size()
        width       = cols - 6

        bar_row     = rows - 3
        x           = 3

        top         = '╭' + '─' * width + '╮'
        middle      = '│' + ' ' * width + '│'
        bottom      = '╰' + '─' * width + '╯'

        stdout.write(f'\033[{bar_row};{x}H'     + top)
        stdout.write(f'\033[{bar_row + 1};{x}H' + middle)
        stdout.write(f'\033[{bar_row + 2};{x}H' + bottom)
        stdout.flush()

    @staticmethod
    def move_cursor_to_input() -> None:
        cols, rows  = get_terminal_size()
        x           = 5
        y           = rows - 2

        stdout.write(f'\033[{y};{x}H> ')
        stdout.flush()
