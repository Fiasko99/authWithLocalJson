__all__ = ['UserService']

from Services import JSONService


class UserService:
    def __init__(self, login, json_service: JSONService):
        self.login = login
        self.json_service = json_service

    def _get_user(self):
        users = self.json_service.get_specific_data_by_key('users')
        for user in users:
            if user['login'] == self.login:
                return user

    def print_profile(self):
        user = self._get_user()
        profiles = self.json_service.get_specific_data_by_key('profiles')
        for profile in profiles:
            if profile['user_id'] == user['id']:
                for k, v in profile.items():
                    print(k, v)

    def print_name(self):
        user = self._get_user()
        print(f'Your name in system: {user["username"]}')

    def get_name(self):
        user = self._get_user()
        return user['username']

    def rename(self):
        new_name = input('Input new name: ')
        self.json_service.refactor_data({"username": new_name, "login": self.login})

    def refactor_password(self):
        new_password = input('Input new password: ')
        self.json_service.refactor_data({"password": new_password, "login": self.login})
