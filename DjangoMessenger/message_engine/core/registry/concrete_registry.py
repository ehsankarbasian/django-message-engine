from .base_registry import BaseRegistry


class PayloadRegistry(BaseRegistry):
    _REGISTRY = {}


class PermissionRegistry(BaseRegistry):
    _REGISTRY = {}


class SenderRegistry(BaseRegistry):
    _REGISTRY = {}
