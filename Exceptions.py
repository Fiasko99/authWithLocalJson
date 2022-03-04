__all__ = ['UserArgsException', 'UserExistException']


class UserArgsException(Exception):
    def __str__(self):
        return 'Wrong user data in args'


class UserExistException(Exception):
    def __str__(self):
        return 'User exist'
