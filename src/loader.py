from json       import load
from typing     import Dict, Iterator
from src.errors import Logger


class Loader:
    @staticmethod
    def load_json(filename: str) -> Dict[str, str]:
        with open(filename, 'r') as f:
            return (load(f))

    @staticmethod
    def _get_plugin_name(filename: str) -> str:
        return (filename.split('/')[-1])

    @staticmethod
    def _load_plugins(commands: Dict[str, str]) -> Iterator[str]:
        prefix: str     = 'plugins/'
        try:
            for i in commands.values():
                with open(i, 'r') as file:
                    yield Loader._get_plugin_name(i)
        except FileNotFoundError:
            Logger.log('ERROR: file not found -> ' + i)
            pass
