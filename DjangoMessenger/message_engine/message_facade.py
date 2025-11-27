from message_engine.core.factory import MessageFactory

from message_engine.message_engine_concrete.builders.verify import VerifyBuilder


class MessageFacade:
    
    def send_verify_message(user, context):
        
        text = VerifyBuilder.get_text(context)
        payload = VerifyBuilder.get_payload_list(context)
        
        sender, identifier = MessageFactory._get_sender(user)
        sender.send(text, payload, identifier)
