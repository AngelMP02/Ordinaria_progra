from tweet import Tweet

class DirectMessage(Tweet):
    def __init__(self, message, sender, receiver):
        super().__init__(message, sender)
        self.receiver = receiver
