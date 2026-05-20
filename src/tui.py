from src.loader import Loader
from shutil     import get_terminal_size
from typing     import List, Dict
from termios    import tcgetattr, tcsetattr, TCSADRAIN
from tty        import setraw
from sys        import stdin, stdout


class MainDisplay:
    @staticmethod
    def draw_border() -> None:
        cols, rows  = get_terminal_size()
        width       = cols - 2

        top         = '╭' + '─' * width + '╮'
        bottom      = '╰' + '─' * width + '╯'
        middle      = '│' + ' ' * width + '│'

        print(top)
        for _ in range(rows - 2):
            print(middle)
        print(bottom, end='')
        stdout.flush()
        PluginView.draw_window()
        CLIBar.draw_bar()

    @staticmethod
    def hide_cursor() -> None:
        with open('config.json', 'r') as f:
            pass
        stdout.write('\033[?25l')
        stdout.flush()

    @staticmethod
    def enable_raw_mode() -> None:
    
        fd          = stdin.fileno()
        old         = tcgetattr(fd)
        setraw(fd)
        buf         = ''
        cols, rows  = get_terminal_size()
        x_start     = 5
        x           = x_start + 2
        y           = rows - 2

        try:
            while True:
                selected    = stdin.read(1)
                if (selected == '\x03'):
                    break

                elif (selected == '\r'):
                    if (buf):
                        CLIBar._handle_command(buf)
                        buf = ''
                    stdout.write(f'\033[{y};{x_start}H' + ' ' * (cols - x_start - 4))
                    stdout.write(f'\033[{y};{x_start}H> ')
                    x   = x_start + 2
                    stdout.flush()

                elif (selected == '\x08' and buf):
                    stripped    = buf.rstrip(' ')
                    last_space  = stripped.rfind(' ')
                    new_buf     = buf[:last_space + 1] if last_space != 1 else ''

                    clear_chars = len(buf) - len(new_buf)
                    x           -= clear_chars
                    stdout.write(f'\033[{y};{x}H' + ' ' * clear_chars)
                    stdout.write(f'\033[{y};{x}H')
                    buf         = new_buf
                    stdout.flush()

                elif (selected == '\x7f' and buf and selected != '\r'):
                    buf = buf[:-1]
                    x   -= 1
                    stdout.write(f'\033[{y};{x}H ')
                    stdout.write(f'\033[{y};{x}H')
                    stdout.flush()

                elif (selected >= ' ' and selected != '\r' and selected != '\x7f'):
                    buf += selected
                    stdout.write(f'\033[{y};{x}H{selected}')
                    x   += 1
                    stdout.flush()

        except KeyboardInterrupt:
            pass
        finally:
            tcsetattr(fd, TCSADRAIN, old)
            stdout.write('\033[?25h')
            stdout.write('\033[H\033[J')
            stdout.flush()


class PluginView:
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
        cmd_list: List[str] = list(
                Loader._load_plugins(Loader.load_json('./config.json')[0]['commands'])
                )
        if (cmd in cmd_list):
            ...

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
