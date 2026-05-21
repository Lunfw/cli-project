from src.errors import Logger
from src.loader import Loader
from typing     import List, Any
from json       import dump
from shutil     import move


class Plugin:
    '''
    _load.py: load <plugin> (.py.bak/.py)

    Takes a .py file and moves it to ./plugins, while also adding it to the config.json as a command to use on the command line.
    '''
    def run(self, args: List[Any], view) -> None:
        error: List[str] = []
        if (not args):
            view.write('Usage: load <plugin>')
            return

        view.write(f'Adding files into config.json')
        config  = Loader.load_json('./config.json')
        prefix  = './plugins/'

        for i in args:
            temp    = i[i.rfind('/') + 1:]
            Logger.log(f'Loading plugin: {temp}', 'INFO')

            if (i.endswith('.bak') and '.py' in i):
                temp    = temp[:-4]
                Logger.log('.bak file found, renaming -> ' + temp, 'WARNING')
            elif (not temp.endswith('.py')):
                Logger.log('Invalid plugin -> ' + temp, 'ERROR')
                error.append(temp)
                continue
            
            if (temp not in config[0]['commands']):
                config[0]['commands'][temp] = './plugins/' + temp
                move(i, prefix + temp)
                Logger.log('Added plugin -> ' + temp, 'SUCCESS')
            else:
                Logger.log('Plugin already in config, skipping -> ' + temp, 'WARNING')

        with open('./config.json', 'w') as f:
            dump(config, f, indent=4)

        if (not len(error)):
            Logger.log('All plugins loaded successfully', 'SUCCESS')
            view.write('Done!')
        else:
            Logger.log('#   Some plugins failed to load', 'ERROR')
            for i in error:
                Logger.log('│   ' + i, 'ERROR')
            view.write('Some files failed to load, check logs for more info.')
