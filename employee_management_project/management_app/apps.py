from django.apps import AppConfig


class ManagementAppConfig(AppConfig):
    name = 'management_app'

    def ready(self):
        from . import signal_handlers