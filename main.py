import os

from typing import Union
from dotenv import load_dotenv

from AppViewer import AppViewer
from Services import JSONService, UserService, AuthService

load_dotenv()
path = os.getenv('PATH_TO_JSON')


def main():
    start = True
    user_service: Union[UserService, None] = None
    json_service = JSONService(path)
    auth_service = AuthService(json_service)
    while start:
        AppViewer.show_main()
        main_option = input("Option (full name with case): ")
        main_options = {
            "Sign in": 'auth',
            "Sign up": 'registration',
        }
        if main_option in main_options.keys():
            user_service: UserService = auth_service.__getattribute__(main_options[main_option])()
        elif main_option == 'quit':
            quit()
        while isinstance(user_service, UserService):
            AppViewer.show_user_panel(user_service.get_name())
            user_option = input("Option (full name with case): ")
            user_options = {
                "Get name": 'print_name',
                "Show profile": 'print_profile',
                "Rename": 'rename',
                "Change password": 'refactor_password'
            }
            if user_option in user_options.keys():
                user_service.__getattribute__(user_options[user_option])()
            elif user_option == 'exit':
                main()


if __name__ == '__main__':
    main()
