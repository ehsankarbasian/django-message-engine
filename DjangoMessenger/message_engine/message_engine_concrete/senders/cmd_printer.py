from message_engine.core.interfaces.sender import SenderInterface


class CmdPrinterSender(SenderInterface):
    _ABSTRACT = False
    
    @staticmethod
    def send(text, payload):
        print()
        print()
        print(50 * '#')
        print()
        print('Sending message ...')
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
