from src.colors import Format
from typing     import List
from shutil     import move


class Plugin:
    def run(self, args: List[str], view) -> None:
        if (not args):
            view.write('Usage: delete <file>')
            return
        prefix: str = './backup'

        view.write(Format.colored('#   Backing up under ./backup/*.py.bak:'), 'WHITE')
        view.write(Format.colored('│    ', 'GREY'))
        for i in args:
            view.write(Format.colored('├──  ' + i, 'GREY'))
            move(i, prefix + i + '.bak')
        view.write(Format.colored('│', 'GREY'))
        view.write('#   Deleted '+ str(len(args)) + ' files')
