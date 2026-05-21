from src.errors import Logger
from typing     import Any


class Plugin:
    def run(self, args: Any, view) -> None:
        Logger.log('_clear.py: Clearing window')
        view.clear()
        return
