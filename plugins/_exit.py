from typing import List


class Plugin:
    def run(self, args: List[str], view) -> None:
        raise KeyboardInterrupt
