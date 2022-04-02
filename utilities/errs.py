class ArduinoConnectionError(Exception):
    pass


class MesssageDecodeError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super(MesssageDecodeError, self).__init__()


class MessageTimeoutError(Exception):
    pass
