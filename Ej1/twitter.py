
class UserAccount:
    def __init__(self, username):
        self.username = username
        self.followers = []
        self.tweets = []

    def follow(self, user2):
        user2.add_follower(self)

    def add_follower(self, follower):
        self.followers.append(follower)

    def tweet(self, tweet1):
        self.tweets.append(tweet1)
        self.notify_followers(tweet1)

    def notify_followers(self, tweet):
        for follower in self.followers:
            follower.receive_tweet(self, tweet)

    def receive_tweet(self, user, tweet):
        # Añade el tweet al timeline del usuario
        # Puedes implementar la lógica adicional según tus necesidades
        pass

