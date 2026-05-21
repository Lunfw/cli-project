from src.colors import Format
from typing     import List
from shutil     import move


class Plugin:
    def run(self, args: List[str], view) -> None:
        if (not args):
            view.write('Usage: add <file>')
            return

        view.write(Format.colored('#    Adding *.py to ./plugins', 'WHITE'))
        view.write(Format.colored('│    ', 'GREY'))
        for i in args:
            view.write(Format.colored('├──  ' + i, 'GREY'))
            if (i.endswith('.bak') and '.py' in i):
                move(i, './plugins/' + i[:-4])
            else:
                move(i, './plugins/' + i)
        view.write(Format.colored('│', 'GREY'))
        view.write('#    Added '+ str(len(args)) + ' files')
