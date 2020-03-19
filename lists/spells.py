from classes.item     import Item

class Spells:
    def __init__(self):
        self.fireball   = Item('spell', 'fireball', 'Файербол', 'Просто огненный шар', 
                            attack=5, cost=10)
        self.heal   = Item('spell', 'heal', 'Лечение малое', 'Лечит небольшие раны', 
                            heal=5, cost=7)
