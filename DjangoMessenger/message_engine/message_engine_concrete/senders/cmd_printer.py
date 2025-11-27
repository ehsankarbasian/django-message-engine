from message_engine.core.interfaces import SenderInterface


class CmdPrinterSender(SenderInterface):
    
    _ABSTRACT = False
    
    @staticmethod
    def send(text, payload, identifier):
        print()
        print()
        print(50 * '#')
        print()
        print(f'Sending message to "{identifier}"')
        print(f'text    : {text}')
        print(f'payload : {payload}')
        print()
        print(f'payload details :')
        for p in payload:
            print(f'object ({p.__class__.__name__}) : {p.__dict__}')
        print()
        print(50 * '#')
        print()
        print()
