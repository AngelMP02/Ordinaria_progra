from datetime import datetime

class Tweet:
    def __init__(self, message, sender):
        self.message = message
        self.sender = sender
        self.time = datetime.now()
