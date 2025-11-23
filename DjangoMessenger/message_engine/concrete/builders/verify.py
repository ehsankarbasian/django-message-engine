from message_engine.core.interfaces.builder import BuilderInterface

from message_engine.concrete.payloads.button import Button


class VerifyBuilder(BuilderInterface):
    
    @staticmethod
    def get_text(context):
        return "Please verify your sender identifier"
    
    @staticmethod
    def get_payload_list(context):
        submit_button = Button(text="Verify", target=None)
        return [submit_button]
