from src.colors import Format
from typing     import List
from shutil     import move


class Plugin:
    '''
    _add.py: add <file> (.py.bak/.py)

    Adds a .py file to ./plugins. Does not add the file to the config.json.
    Mainly for adding custom libs for plugins.
    '''
    def run(self, args: List[str], view) -> None:
        temp: List[str] = []

        if (not args):
            view.write('Usage: add <file>')
            Logger.log('No file provided, closing', 'WARNING')
            return

        view.write(Format.colored('#    Adding *.py to ./plugins', 'WHITE'))
        view.write(Format.colored('│    ', 'GREY'))
        for i in args:
            view.write(Format.colored('├──  ' + i, 'GREY'))
            if (i.endswith('.bak') and '.py' in i):
                move(i, './plugins/' + i[:-4])
            else:
                move(i, './plugins/' + i)
            temp.append(i)
        view.write(Format.colored('│', 'GREY'))
        view.write('#    Added '+ str(len(args)) + ' files')
        
        Logger.log('#   Added ' + str(len(args)) + ' files', 'SUCCESS')
        for i in temp:
            Logger.log('│   ' + i, 'INFO')
