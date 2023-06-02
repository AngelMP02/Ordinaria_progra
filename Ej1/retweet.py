from tweet import Tweet

class Retweet(Tweet):
    def __init__(self, message, sender, tweet):
        super().__init__(message, sender)
        self.retweeted_tweet = tweet
    def __str__(self):
            return f"Retweet from {self.sender.username} at {self.time}: {self.message}\nOriginal Tweet: {self.retweeted_tweet}"