from src.colors import Format
from typing import List
from os     import listdir


class Plugin:
    def run(self, args: List[str], view) -> None:
        view.write(Format.colored('#    ./plugins/', 'WHITE'))
        temp: List[str] = []
        for f in listdir('./plugins'):
            if (not f.startswith('_')):
                temp.append(f)

        if (not len(temp)):
            view.write('No plugins found!')
            return

        for i in temp:
            view.write(Format.colored('│    ', 'GREY'))
            view.write(Format.colored('├──  ' + i, 'GREY'))
        view.write(Format.colored('│', 'GREY'))
        view.write('#    ' + str(len(temp)) + ' file(s)')
