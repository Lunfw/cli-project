from src.errors import Logger
from typing import List


class Plugin:
    '''
    _cat.py: cat <file>

    Prints a file to the screen.
    '''
    def run(self, args: List[str], view) -> None:
        if (not args):
            view.write('Usage: cat <file>')
            Logger.log('No file provided, closing', 'WARNING')
            return
        Logger.log('Reading file -> ' + args[0])
        with open(args[0], "r") as f:
            for line in f:
                view.write(line.rstrip('\n'))
        Logger.log('Closing file -> '+ args[0])
