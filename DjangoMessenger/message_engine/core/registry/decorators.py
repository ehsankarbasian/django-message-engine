# core/registry/decorators.py
from .sender import SenderRegistry
from .permission import PermissionRegistry
from .payload import PayloadRegistry


def register_sender(cls):
    SenderRegistry.register(cls.__name__, cls)
    return cls


def register_permission(cls):
    PermissionRegistry.register(cls.__name__, cls)
    return cls


def register_payload(cls):
    PayloadRegistry.register(cls.__name__, cls)
    return cls
