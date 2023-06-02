from datetime import datetime

class Tweet:
    MAX_CHARACTERS = 140

    def __init__(self, message, sender):
        if len(message) > self.MAX_CHARACTERS:
            raise ValueError("El mensaje excede los 140 caracteres.")
        self.message = message
        self.sender = sender
        self.time = datetime.now()
    def __str__(self):
        return f"Tweet from {self.sender.username} at {self.time}: {self.message}"
