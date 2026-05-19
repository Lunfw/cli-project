from shutil     import get_terminal_size
from typing     import List
from termios    import tcgetattr, tcsetattr, TCSADRAIN
from tty        import setraw
from sys        import stdin, stdout
from signal     import signal, SIGINT


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

    @staticmethod
    def handle_exit(sig, frame) -> None:
        if (_original_settings):
            tcsetattr(stdin, TCSADRAIN, _original_settings)
        stdout.write('\033[H\033[J')
        stdout.flush()
        exit(0)

    @staticmethod
    def enable_raw_mode() -> None:
        fd = stdin.fileno()
        old = tcgetattr(fd)
        setraw(fd)
        selected = stdin.read(1)
        tcsetattr(fd, TCSADRAIN, old)
        if (selected == '\x03'):
            return
