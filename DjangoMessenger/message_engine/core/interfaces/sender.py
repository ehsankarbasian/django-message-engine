from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from message_engine.core.interfaces.payload import PayloadItemInterface

from ..registry.metaclass import AutoRegisterMeta
from ..registry.concrete_registry import SenderRegistry


class SenderInterface(ABC, metaclass=AutoRegisterMeta):
    _ABSTRACT = True
    registry = SenderRegistry
    
    @staticmethod
    @abstractmethod
    def send(text: str, payload: PayloadItemInterface):
        pass
