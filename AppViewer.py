__all__ = ['AppViewer']


class AppViewer:
    @staticmethod
    def show_main():
        print("Select option:")
        print("\t Sign in")
        print("\t Sign up")
        print("\t quit")

    @staticmethod
    def show_user_panel(name):
        print(f'Welcome {name}! Select option:')
        print("\t Get name")
        print("\t Show profile")
        print("\t Rename")
        print("\t Change password")
        print('\t exit')
