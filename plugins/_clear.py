from typing import Any


class Plugin:
    def run(self, args: Any, view) -> None:
        view.clear()
        return
