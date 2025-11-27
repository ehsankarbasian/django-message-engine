from message_engine.core.service import MessageService

from message_engine.message_engine_concrete.builders import VerifyBuilder, WelcomeBuilder


class MessageFacade:
    
    @staticmethod
    def send_verify_message(user, context):
        MessageService.send(user, context, VerifyBuilder)
    
    @staticmethod
    def senf_welcome_message(user, context):
        MessageService.send(user, context, WelcomeBuilder)
