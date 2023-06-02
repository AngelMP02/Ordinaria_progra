from tweet import Tweet
from retweet import Retweet
from direct_message import DirectMessage
from Ej1.twitter import UserAccount

if __name__ == '__main__':
    # Crear usuarios
    user1 = UserAccount("user1")
    user2 = UserAccount("user2")
    user3 = UserAccount("user3")

    # Seguir a otros usuarios
    user1.follow(user2)
    user1.follow(user3)

    # Enviar tweets
    tweet1 = Tweet("Hello, world!", user1)
    user1.tweet(tweet1)

    tweet2 = Tweet("I'm having a great day!", user2)
    user2.tweet(tweet2)

    # Enviar retweets
    retweet1 = Retweet("Great tweet!", user1, tweet2)
    user1.tweet(retweet1)

    retweet2 = Retweet("Nice tweet!", user3, tweet1)
    user3.tweet(retweet2)

    # Enviar mensajes directos
    direct_message1 = DirectMessage("Private message", user1, user2)
    user1.tweet(direct_message1)

    direct_message2 = DirectMessage("Another private message", user3, user1)
    user3.tweet(direct_message2)

    # Imprimir timeline de cada usuario
    print(f"Timeline de {user1.username}:")
    for tweet in user1.tweets:
        print(tweet)

    print(f"Timeline de {user2.username}:")
    for tweet in user2.tweets:
        print(tweet)

    print(f"Timeline de {user3.username}:")
    for tweet in user3.tweets:
        print(tweet)
