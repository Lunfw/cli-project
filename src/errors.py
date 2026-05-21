from src.colors import Format
from datetime   import datetime


class Logger:
    @staticmethod
    def log(text: str, code: str = 'INFO') -> None:
        timestamp: str  = datetime.now().strftime('%H:%M:%S')
        prefix: str     = '[' + timestamp + ']    │ '
        logname: str    = 'logs_' + datetime.now().strftime('%Y-%m-%d')
        text: str       = ': ' + text
        wrapper: str    = Format.colored(prefix + code + text, 'CYAN')

        if (code == 'SUCCESS' or code == 'EXIT'):
            wrapper = Format.colored(prefix + code + text, 'GREEN')
        if (code == 'ERROR'):
            wrapper = Format.colored(prefix + code + text, 'RED')
        elif (code == 'WARNING'):
            wrapper = Format.colored(prefix + code + text, 'YELLOW')

        with open('Logs/' + logname, 'a') as fd:
            print(wrapper, file=fd)
