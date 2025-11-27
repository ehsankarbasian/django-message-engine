from abc import ABC, abstractmethod

# from models import *

from ..registry.metaclass import AutoRegisterMeta
from ..registry.concrete_registry import PermissionRegistry


class PermissionInterface(ABC, metaclass=AutoRegisterMeta):
    _ABSTRACT = True
    _REGISTRY = PermissionRegistry
    
    @staticmethod
    @abstractmethod
    def has_permission(user) -> bool:
        pass
