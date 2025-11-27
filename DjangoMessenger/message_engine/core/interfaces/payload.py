from abc import ABC

from ..registry.metaclass import AutoRegisterMeta
from ..registry.concrete_registry import PayloadRegistry


class PayloadItemInterface(ABC, metaclass=AutoRegisterMeta):
    _ABSTRACT = True
    _REGISTRY = PayloadRegistry
