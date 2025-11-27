from message_engine.core.service import MessageService

from message_engine.message_engine_concrete.builders.verify import VerifyBuilder


class MessageFacade:
    
    @staticmethod
    def send_verify_message(user, context):
        MessageService.send(user, context, VerifyBuilder)
