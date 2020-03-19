from classes.creatures.parent     import Somebody
from lists.items                  import Items
import random

class Hero(Somebody):
    def __init__(self, name):

        self.exp        = 0
        self.level      = 0
        self.money      = 100
        self.inventory  = Inventory()
    
class Inventory:
    def __init__(self):
        items = Items()
        self.head       = items.init_cap
        self.right_hand = items.init_sword
        self.left_hand  = items.init_sheild
        self.cheast     = items.init_brp
        self.pants      = items.init_pants
        self.boots      = items.init_boots
        self.backpack   = []


