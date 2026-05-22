from json       import load
from typing     import Dict, Iterator, List
from pathlib    import Path
from importlib  import util
from src.errors import Logger


def run(args: List[str], view) -> None:
    prefix  = './plugins/'
    if (not args):
        view.write('Usage: load <plugin>')
        return

    path = Path(prefix + args[0] + '.py')
    try:
        if (not path.exists(path)):
            view.write('ERROR: plugin not found ->' + args[0])
            raise FileNotFoundError
        spec    = util.spec_from_file_location(args[0], path)
        module  = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        view.clear()
        module.run(view)
    except FileNotFoundError:
        Logger.log('ERROR: plugin not found -> ' + args[0])
        pass


class Loader:
    @staticmethod
    def load_json(filename: str) -> Dict[str, str]:
        with open(filename, 'r') as f:
            return (load(f))

    @staticmethod
    def _load_plugins(commands: Dict[str, str]) -> Iterator[str]:
        try:
            for name, path in commands.items():
                if (Path(path).exists()):
                    yield name, path
                else:
                    raise FileNotFoundError
        except FileNotFoundError:
            Logger.log('ERROR: file not found -> ' + i)
            Logger.separate()
            pass
