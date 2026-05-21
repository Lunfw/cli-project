from src.colors import Format
from datetime   import datetime


class Logger:
    @staticmethod
    def log(text: str, code: str = 'INFO') -> None:
        sign: str       = '. '
        timestamp: str  = datetime.now().strftime('%H:%M:%S')
        prefix: str     = '[' + timestamp + ']    │ '
        logname: str    = 'logs_' + datetime.now().strftime('%Y-%m-%d')
        text: str       = ': ' + text
        wrapper: str    = Format.colored(sign + prefix + code + text, 'CYAN')

        if (code == 'SUCCESS' or code == 'EXIT'):
            sign = '+ '
            wrapper = Format.colored(sign + prefix + code + text, 'GREEN')
        if (code == 'ERROR'):
            sign = '- '
            wrapper = Format.colored(sign + prefix + code + text, 'RED')
        elif (code == 'WARNING'):
            sign = '~ '
            wrapper = Format.colored(sign + prefix + code + text, 'YELLOW')

        with open('Logs/' + logname, 'a') as fd:
            print(wrapper, file=fd)

    @staticmethod
    def separate() -> None:
        logname: str    = 'logs_' + datetime.now().strftime('%Y-%m-%d')
        with open('Logs/' + logname, 'a') as fd:
            print('\n', end='', file=fd)
