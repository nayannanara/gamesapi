class BaseException(Exception):
    message: str = 'Internal Server Error'

    def __init__(self: 'BaseException', message: str) -> None:
        self.message = message


class DatabaseException(BaseException):
    pass
