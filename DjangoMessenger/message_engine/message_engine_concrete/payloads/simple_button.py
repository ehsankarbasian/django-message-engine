from message_engine.core.interfaces import AbstractPayloadItem


class SimpleButton(AbstractPayloadItem):
    
    def __init__(self, text, target):
        self.text = text
        self.target = target
