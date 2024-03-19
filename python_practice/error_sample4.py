class PracticeBookError(Exception):
    pass


class PageNotFoundError(PracticeBookError):
    def __init__(self, message):
        self.message = message
