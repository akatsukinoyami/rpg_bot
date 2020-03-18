from classes.creature import Somebody
import random

class Hero(Somebody): #to love
    def __init__(self, name):

        self.exp        = 0
        self.level      = 0
        
        self.right_hand = None
        self.left_hand  = None
    
    