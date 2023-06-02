from tweet import Tweet

class Retweet(Tweet):
    def __init__(self, message, sender, tweet):
        super().__init__(message, sender)
        self.retweeted_tweet = tweet
