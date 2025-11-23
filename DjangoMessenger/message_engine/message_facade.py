from message_engine.core.factory import MessageFactory


class MessageFacade:
    
    def send_verify_message(user):
        MessageFactory.create(user, context=None)
