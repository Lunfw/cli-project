from src.colors import Format
from src.errors import Logger
from typing     import List
from os         import listdir


class Plugin:
    '''
    _ls.py: ls

    Lists ./*.py plugins that are not _*.py.
    '''
    def run(self, args: List[str], view) -> None:
        view.write(Format.colored('#    ./plugins/', 'WHITE'))
        temp: List[str] = []
        for f in listdir('./plugins'):
            if (not f.startswith('_')):
                temp.append(f)

        if (not len(temp)):
            view.write('No plugins found!')
            Logger.log('No plugins found', 'WARNING')
            return

        for i in temp:
            view.write(Format.colored('│    ', 'GREY'))
            view.write(Format.colored('├──  ' + i, 'GREY'))
        view.write(Format.colored('│', 'GREY'))
        view.write('#    ' + str(len(temp)) + ' file(s)')
