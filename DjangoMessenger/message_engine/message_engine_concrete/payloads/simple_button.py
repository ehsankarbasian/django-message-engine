from message_engine.core.interfaces.payload import PayloadItemInterface


class SimpleButton(PayloadItemInterface):
    
    def __init__(self, text, target):
        self.text = text
        self.target = target
