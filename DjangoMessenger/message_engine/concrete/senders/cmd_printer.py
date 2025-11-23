from message_engine.core.interfaces.sender import SenderInterface


class CmdPrinterSender(SenderInterface):
    
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
        print(50 * '#')
        print()
        print()
