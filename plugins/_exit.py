from typing import List


class Plugin:
    '''
    _exit.py: exit

    Sends an exit signal and interrupts the program.
    '''
    def run(self, args: List[str], view) -> None:
        raise KeyboardInterrupt
