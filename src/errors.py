from datetime import datetime


class Logger:
    @staticmethod
    def log(text: str) -> None:
        timestamp: str  = datetime.now().strftime('%H:%M:%S')
        prefix: str     = '[' + timestamp + ']    │ '
        logname: str    = 'logs_' + datetime.now().strftime('%Y-%m-%d')
        with open('Logs/' + logname, 'a') as fd:
            print(prefix + text, file=fd)
