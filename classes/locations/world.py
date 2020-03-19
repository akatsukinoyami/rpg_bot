from classes.creatures.hero import Hero

class World:
    def __init__(self, username):
        self.hero   = Hero(username)
        self.battle = None