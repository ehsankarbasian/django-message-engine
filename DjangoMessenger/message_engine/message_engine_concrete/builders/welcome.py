from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.message_engine_concrete.permissions import Verified


class WelcomeBuilder(BuilderInterface):
    
    permissions = (Verified, )
    
    @staticmethod
    def get_text(context):
        return "Welcome dear user"
    
    @staticmethod
    def get_payload_list(context):
        return list()
