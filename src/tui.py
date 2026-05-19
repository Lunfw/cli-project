from shutil     import get_terminal_size
from typing     import List
from termios    import tcgetattr, tcsetattr, TCSADRAIN
from tty        import setraw
from sys        import stdin


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
