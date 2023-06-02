class UserAccount:
    def __init__(self, alias, email):
        self.alias = alias  # Alias del usuario
        self.email = email  # Email de contacto
        self.tweets = []  # Lista de tweets publicados por el usuario
        self.followers = []  # Lista de seguidores del usuario
        self.timeline = []  # Timeline del usuario (conjunto de tweets recibidos)
    def follow(self, user2):
            user2.add_follower(self)

    def add_follower(self, follower):
        self.followers.append(follower)