from message_engine.core.interfaces.sender import SenderInterface
from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.concrete.senders.cmd_printer import CmdPrinterSender

from message_engine.models import *


class MessageFactory:
    
    def create(user, context, builder):
        pass
    
    def _get_sender(user):
        # TODO: Read from the DataBase
        return CmdPrinterSender
