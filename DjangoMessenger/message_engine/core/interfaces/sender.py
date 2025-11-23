from abc import ABC, abstractmethod

from message_engine.core.interfaces.payload import PayloadItemInterface


class SenderInterface(ABC):
    
    @staticmethod
    @abstractmethod
    def send(text, payload):
        pass
