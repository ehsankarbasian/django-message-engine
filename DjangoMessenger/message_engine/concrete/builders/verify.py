from message_engine.core.interfaces.builder import BuilderInterface


class VerifyBuilder(BuilderInterface):
    
    @staticmethod
    def get_text(context):
        return "Please verify your sender identifier"
    
    @staticmethod
    def get_payload(context):
        # TODO: add a Button
        return None
