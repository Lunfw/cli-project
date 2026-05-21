from src.loader     import Loader
from src.errors     import Logger
from src.regions    import CLIBar, PluginView
from shutil         import get_terminal_size
from typing         import List, Dict
from termios        import tcgetattr, tcsetattr, TCSADRAIN, ICANON, ECHO, IEXTEN, VMIN, VTIME
from sys            import stdin, stdout
from importlib      import util
from os             import path, listdir


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
        fd              = stdin.fileno()
        old             = tcgetattr(fd)
        new             = tcgetattr(fd)
        new[3]          &= ~(ICANON | ECHO | IEXTEN)
        new[6][VMIN]    = 1
        new[6][VTIME]   = 0
        tcsetattr(fd, TCSADRAIN, new)
        buf             = ''
        cols, rows      = get_terminal_size()
        x_start         = 5
        x               = x_start + 2
        y               = rows - 2

        try:
            while True:
                selected    = stdin.read(1)

                if (selected == '\t'):
                    parts   = buf.strip().split()

                    if (not parts):
                        pass
                    elif (len(parts) == 1):
                        commands    = Loader.load_json('./config.json')[0]['commands']
                        matches     = [k for k in commands if k.startswith(parts[0])]
                    else:
                        partial     = parts[-1]
                        parent      = path.dirname(partial) if path.dirname(partial) else '.'
                        prefix      = path.basename(partial)

                        try:
                            matches = [
                                    path.join(parent, f) if parent != '.' else f
                                    for f in listdir(parent)
                                    if f.startswith(prefix)
                                ]
                        except FileNotFoundError:
                            matches == []
                        
                    if (len(matches) == 1):
                        completion  = matches[0][len(parts[-1]):]
                        buf         += completion
                        stdout.write(f'\033[{y};{x}H{completion}')
                        x           += len(completion)
                        stdout.flush()
                    elif (len(matches) > 1):
                        PluginView.clear()
                        for match in matches:
                            PluginView.write(match)

                if (selected == '\n'):
                    PluginView.clear()
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

                elif (selected == '\x7f' and buf and selected != '\n'):
                    buf = buf[:-1]
                    x   -= 1
                    stdout.write(f'\033[{y};{x}H ')
                    stdout.write(f'\033[{y};{x}H')
                    stdout.flush()

                elif (selected >= ' ' and selected != '\n' and selected != '\x7f'):
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
