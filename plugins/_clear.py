from typing import Any


class Plugin:
    def run(self, args: Any, view) -> bool:
        view.clear()
        return True
