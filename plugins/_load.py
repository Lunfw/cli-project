from typing import List, Any


class Plugin:
    def run(self, args: List[Any], view) -> None:
        if (not args):
            view.write('Usage: load <plugin>')
            return

        view.write(f'Loading {args[0]}...')

