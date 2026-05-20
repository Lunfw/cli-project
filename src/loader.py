from json       import load
from typing     import Dict


class Loader:
    @staticmethod
    def load(filename: str) -> str:
        with open(filename) as f:
            text    = f.read()
        return (load(text))

    @staticmethod
    def load_plugins() -> None:
        pass
