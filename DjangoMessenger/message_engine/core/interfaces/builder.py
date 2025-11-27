from typing import List
from abc import ABC, abstractmethod

from message_engine.core.interfaces.payload import PayloadItemInterface
# from ..registry.concrete_registry import 


class BuilderInterface(ABC):
    
    @staticmethod
    @abstractmethod
    def get_text(context) -> str:
        pass
    
    @staticmethod
    @abstractmethod
    def get_payload_list(context) -> List[PayloadItemInterface]:
        pass
