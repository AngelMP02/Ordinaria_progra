from tweet import Tweet
from retweet import Retweet
from direct_message import DirectMessage
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

# Ejemplo de uso:
user1 = UserAccount("user1")
user2 = UserAccount("user2")

tweet1 = Tweet("¡Hola, este es mi primer tweet!", user1)
print(tweet1.message)  # "¡Hola, este es mi primer tweet!"
print(tweet1.sender)  # user1
print(tweet1.time)  # Instancia de la clase datetime con el momento actual

retweet1 = Retweet("¡Me encanta este tweet!", user2, tweet1)
print(retweet1.message)  # "¡Me encanta este tweet!"
print(retweet1.sender)  # user2
print(retweet1.time)  # Instancia de la clase datetime con el momento actual
print(retweet1.retweeted_tweet)  # Instancia del Tweet original (tweet1)

dm = DirectMessage("¡Hola! ¿Cómo estás?", user1, user2)
print(dm.message)  # "¡Hola! ¿Cómo estás?"
print(dm.sender)  # user1
print(dm.time)  # Instancia de la clase datetime con el momento actual
print(dm.receiver)  # user2