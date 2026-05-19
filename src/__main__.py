from src.colors import Format
from src.errors import GeneralErrors
from src.tui    import MainDisplay


#   Main
class Main:
    def __init__(self) -> None:
        MainDisplay.draw_border()
        

if (__name__ == '__main__'):
    try:
        Main()
    except Exception:
        exit(1)
    exit(0)
