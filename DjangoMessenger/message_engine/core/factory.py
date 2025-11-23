from message_engine.core.interfaces.sender import SenderInterface
from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.models import *


class MessageFactory:
    
    def create(user, context):
        pass
    
    def _get_sender(user):
        pass
    
    def _get_builder(user, context):
        pass
