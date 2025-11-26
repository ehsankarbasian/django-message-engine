from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class MessageEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "message_engine"
    
    def ready(self):
        autodiscover_modules('message_engine_concrete')


"""
Recommended structure to client's app:

my_app/
    message_engine_concrete/
        senders.py
        permissions.py
        payloads.py
        builders.py
"""
