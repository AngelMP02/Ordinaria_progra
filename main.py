from direct_message import DirectMessage
from tweet import Tweet
from retweet import Retweet

if __name__ == '__main__':
    if __name__ == '__main__':
     user1 = Tweet("Hello, world!", "user1")
     user2 = Tweet("Hi there!", "user2")

    tweet1 = Tweet("Hello, world!", "user1")
    user1.tweet(tweet1)

    retweet1 = Retweet("Great tweet!", "user2", tweet1)
    user2.retweet(retweet1)

    direct_message = DirectMessage("Private message", "user1", "user2")

    print(tweet1)
    print(retweet1)
    print(direct_message)