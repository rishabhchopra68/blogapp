from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):     # import signals for users
        import users.signals

