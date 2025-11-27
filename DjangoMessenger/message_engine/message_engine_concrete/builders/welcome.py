from message_engine.core.interfaces.builder import BuilderInterface


class WelcomeBuilder(BuilderInterface):
    
    @staticmethod
    def get_text(context):
        return "Welcome dear user"
    
    @staticmethod
    def get_payload_list(context):
        return list()
