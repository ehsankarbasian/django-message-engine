from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.message_engine_concrete.payloads import SimpleButton
from message_engine.message_engine_concrete.permissions import NotVerified, AllowAny


class VerifyBuilder(BuilderInterface):
    
    permissions = (AllowAny, )
    
    @staticmethod
    def get_text(context):
        return "Please verify your sender identifier"
    
    @staticmethod
    def get_payload_list(context):
        submit_button = SimpleButton(text="Verify", target=None)
        return [submit_button]
