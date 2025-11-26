from .sender import SenderRegistry
from .permission import PermissionRegistry
from .payload import PayloadRegistry

from ..interfaces.sender import SenderInterface
from ..interfaces.permission import PermissionInterface
from ..interfaces.payload import PayloadInterface


def register(cls):
    """
    Smart decorator that detects class type and registers it
    in the correct registry.
    """

    # Sender
    if issubclass(cls, SenderInterface):
        SenderRegistry.register(cls.__name__, cls)
        return cls

    # Permission
    if issubclass(cls, PermissionInterface):
        PermissionRegistry.register(cls.__name__, cls)
        return cls

    # Payload
    if issubclass(cls, PayloadInterface):
        PayloadRegistry.register(cls.__name__, cls)
        return cls

    # Unknown class type
    raise TypeError(
        f"@register: class '{cls.__name__}' is not a valid message engine component "
        f"(must inherit from SenderInterface, PermissionInterface or PayloadInterface)."
    )
