from typing import Tuple

from message_engine.core.interfaces.sender import SenderInterface
from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.message_engine_concrete.senders.cmd_printer import CmdPrinterSender

from message_engine.models import *
from message_engine.core.registry.concrete_registry import PayloadRegistry, PermissionRegistry, SenderRegistry


class MessageFactory:
    
    @classmethod
    def create(cls, user, context, builder):
        pass
    
    @staticmethod
    def _get_sender(user) -> Tuple[SenderInterface, str]:
        
        endpoint = (
            MessageEndpoint.objects
                .filter(user=user, is_active=True)
                .order_by("priority")
                .first()
        )
        
        identifier = endpoint.identifier
        sender = SenderRegistry.get(endpoint.endpoint_type)
        
        # TODO: Refactor identifier DataFlow
        return sender, identifier
