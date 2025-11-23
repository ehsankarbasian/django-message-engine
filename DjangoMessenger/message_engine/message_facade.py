from message_engine.core.factory import MessageFactory

from message_engine.concrete.builders.verify import VerifyBuilder


class MessageFacade:
    
    def send_verify_message(user, context):
        text = VerifyBuilder.get_text(context)
        payload = VerifyBuilder.get_payload(context)
        
        sender = MessageFactory._get_sender(user)
        
        sender.send(text, payload)
