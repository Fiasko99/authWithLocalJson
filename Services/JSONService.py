__all__ = ['JSONService']

import json

from DecoratorsForJSONService import DecoratorsForJSONService


class JSONService:
    @DecoratorsForJSONService.validate_json_file
    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json

    def _get_data(self) -> dict:
        with open(self.path_to_json, mode='r') as file:
            return json.loads(file.read())

    def get_specific_data_by_key(self, key: str) -> dict:
        data = self._get_data()
        return data[key]

    def input_data(self, data: dict):
        with open(self.path_to_json, 'w') as file:
            file.write(json.dumps(data))
            return True

    def post_specific_data_by_key(self, key: str, data: dict):
        options = {
            "create_new_user": self.create_new_user,
            "refactor_username": self.refactor_data,
            "auth": self.auth
        }
        return options[key](data)

    @DecoratorsForJSONService.validate_new_user
    def create_new_user(self, user: dict) -> bool:
        data = self._get_data()
        user_id = data['users'][-1]['id'] + 1 if len(data['users']) > 0 else 1
        user['id'] = user_id
        data['users'].append(user)
        new_profile = {
            "user_id": user_id,
            "hp": 100,
            "attack": 15
        }
        data['profiles'].append(new_profile)
        return self.input_data(data) or False

    def refactor_data(self, new_data: dict) -> str:
        data = self._get_data()
        for index in range(len(data['users'])):
            if data['users'][index]['login'] == new_data['login']:
                for k, v in new_data.items():
                    data['users'][index][k] = v
        return "Done!" if self.input_data(data) else "System error"

    def auth(self, data: dict):
        users = self.get_specific_data_by_key('users')
        for user in users:
            if user['login'] == data['login'] and user['password'] == data['password']:
                return True
        return False
