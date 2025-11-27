from typing import Tuple

from message_engine.core.interfaces.sender import SenderInterface
from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.models import MessageEndpoint
from message_engine.core.registry.concrete_registry import SenderRegistry


class MessageService:
    
    @staticmethod
    def send(user, context, builder_class: BuilderInterface):
        
        # Permission check
        for permission in getattr(builder_class, "permissions", []):
            if not permission.has_permission(user):
                raise PermissionError(f"Not allowed for {builder_class.__name__}")

        # Build text and payload
        text = builder_class.get_text(context)
        payload = builder_class.get_payload_list(context)

        # Pick sender and identifier from DB and registry
        sender, identifier = MessageService._get_sender(user)

        # Send
        sender.send(text, payload, identifier)

    
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
