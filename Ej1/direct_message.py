from tweet import Tweet

class DirectMessage(Tweet):
    def __init__(self, message, sender, receiver):
        super().__init__(message, sender)
        self.receiver = receiver
    def __str__(self):
        return f"Direct Message from {self.sender.username} to {self.receiver.username} at {self.time}: {self.message}"