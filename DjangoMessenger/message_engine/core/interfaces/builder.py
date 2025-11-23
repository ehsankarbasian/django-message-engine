from abc import ABC, abstractmethod

from message_engine.core.interfaces.payload import PayloadItemInterface


class BuilderInterface(ABC):
    
    @staticmethod
    @abstractmethod
    def get_text(context):
        pass
    
    @staticmethod
    @abstractmethod
    def get_payload_list(context):
        pass
