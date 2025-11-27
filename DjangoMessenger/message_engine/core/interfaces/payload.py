from abc import ABC

from ..registry.metaclass import AutoRegisterMeta
from ..registry.concrete_registry import PayloadRegistry
from ..registry.base_registry import BaseRegistry


class AbstractPayloadItem(ABC, metaclass=AutoRegisterMeta):
    """
    A minimal helper base class — provides default validate implementation
    (no-op) and a helper to normalize dict output.
    
    A Payload is a structured representation of message content.
    """
    
    _ABSTRACT: bool = True
    _REGISTRY: BaseRegistry = PayloadRegistry

    def validate(self) -> None:
        """
        Validate internal structure.
        Should raise ValueError / TypeError on invalid payload.
        
        default: nothing to validate
        concrete classes should override and raise Exception on invalid data
        """
        pass

    @property
    def payload_type(self) -> str:
        """ Payload name for registry (such as 'SimpleButton', 'Form', ...) """
        return self.__class__.__name__
