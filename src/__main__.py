from src.colors import Format
from src.errors import GeneralErrors

#   Main
class Main:
    def __init__(self) -> None:
        print('hi')

#   Sub-Main
class Sub:
    pass


if (__name__ == '__main__'):
    try:
        Main()
    except Exception:
        exit(1)
    exit(0)
