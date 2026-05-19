class GeneralErrors(Exception):
    pass

class ExitError(GeneralErrors):
    pass

class UnexpectedError(GeneralErrors):
    pass

class DisplayError(GeneralErrors):
    pass
