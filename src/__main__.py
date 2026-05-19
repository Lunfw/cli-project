from src.colors import Format
from src.errors import GeneralErrors
from src.tui    import MainDisplay
from time       import sleep


#   Main
class Main:
    def __init__(self) -> None:
        MainDisplay.draw_border()
        MainDisplay.enable_raw_mode()
        

if (__name__ == '__main__'):
    try:
        Main()
    except Exception:
        exit(1)
    print(Format.colored('Bye', 'WHITE'))
    sleep(1)
    exit(0)
