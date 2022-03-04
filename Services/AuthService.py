__all__ = ['AuthService']

from typing import Union

from .JSONService import JSONService
from .UserService import UserService


class AuthService:
    def __init__(self, json_service):
        self.json_service: JSONService = json_service

    def auth(self) -> Union[UserService, None]:
        try:
            login = input('Input login: ')
            password = input('Input password: ')
            user = {
                "login": login,
                "password": password
            }
            if self.json_service.auth(user):
                return UserService(login, self.json_service)
        except Exception as e:
            print(e)

    def registration(self) -> Union[UserService, None]:
        try:
            login = input('Input login: ')
            password = input('Input password: ')
            username = input('Input username: ')
            user = {
                "login": login,
                "password": password,
                "username": username
            }
            if self.json_service.create_new_user(user):
                return UserService(login, self.json_service)
        except Exception as e:
            print(e)
