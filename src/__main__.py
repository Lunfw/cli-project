from src.colors import Format
from src.tui    import MainDisplay, CLIBar, PluginView
from time       import sleep
from sys        import stdout, argv
from enum       import Enum
from typing     import Tuple, List


class Config(Enum):
    pass


class CheckArgs:
    @staticmethod
    def __arg_exists(arg: List[str]) -> None:
        allowed: Tuple[str] = (
                '--debug',
                '--plugins',
                '--help',
                '--config'
                )

        temp: List[str] = []

        for i in arg:
            if (i in allowed):
                temp.append(i)

    @staticmethod
    def __debug_mode() -> None:
        pass

    @staticmethod
    def __plugins_mode() -> None:
        pass

    @staticmethod
    def __help_mode() -> None:
        pass

    @staticmethod
    def __config_mode() -> None:
        pass


class Main:
    def __init__(self) -> None:
        # MainDisplay.hide_cursor()
        MainDisplay.draw_border()
        CLIBar.move_cursor_to_input()
        MainDisplay.enable_raw_mode()
        # stdout.write('\033[?25h')
        stdout.flush()


if (__name__ == '__main__'):
    try:
        Main()
    except Exception:
        exit(1)
    print(Format.colored('\n# Goodbye!!', 'WHITE'))
    sleep(1)
    exit(0)
