__all__ = ['DecoratorsForJSONService']

import json
import os

from dotenv import load_dotenv

from Exceptions import UserArgsException, UserExistException
from Services import JSONService

load_dotenv()
path = os.getenv('PATH_TO_JSON')


class DecoratorsForJSONService:
    @staticmethod
    def validate_json_file(f):
        default = {
            "users": [],
            "profiles": []
        }

        def exist_keys(data: dict):
            for k in default.keys():
                if k not in data.keys():
                    return False
            return True

        def is_json(json_str):
            try:
                json.loads(json_str)
            except ValueError:
                return False
            return True

        def validate_file():
            data = open(path, 'r').read()
            if not os.path.isfile(path):
                return True
            if not data:
                return True
            if not is_json(data):
                return True
            if not exist_keys(json.loads(data)):
                return True
            return False

        def wrapper(*args, **kwargs):
            if validate_file():
                open(path, mode='w').write(json.dumps(default))
            return f(*args, **kwargs)

        return wrapper

    @staticmethod
    def validate_new_user(f):
        def validate_args(user):
            if len(user['login']) < 4:
                return False
            if len(user['password']) < 4:
                return False
            if len(user['username']) < 6:
                return False
            return True

        def exist_user(user):
            json_file = JSONService(path)
            users = json_file.get_specific_data_by_key('users')
            for i in users:
                if i['login'] == user['login']:
                    return True
            return False

        def wrapper(*args, **kwargs):
            if not validate_args(args[1]):
                raise UserArgsException
            if exist_user(args[1]):
                raise UserExistException
            return f(*args, **kwargs)

        return wrapper
