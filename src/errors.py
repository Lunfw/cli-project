from datetime import datetime


class Logger:
    @staticmethod
    def log(text: str) -> None:
        prefix: str = '[' + datetime.now().strftime('%H:%M:%S') + ']    '
        with open('logs.txt', 'a') as fd:
            print(prefix + text, file=fd)
