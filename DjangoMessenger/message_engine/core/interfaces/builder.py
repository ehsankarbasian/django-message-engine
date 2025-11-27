from typing import List, Tuple
from abc import ABC, abstractmethod

from message_engine.core.interfaces import AbstractPayloadItem, PermissionInterface
# from ..registry.concrete_registry import 


class BuilderInterface(ABC):
    
    permissions: Tuple [PermissionInterface] = ()
    
    @staticmethod
    @abstractmethod
    def get_text(context) -> str:
        pass
    
    @staticmethod
    @abstractmethod
    def get_payload_list(context) -> List[AbstractPayloadItem]:
        pass
