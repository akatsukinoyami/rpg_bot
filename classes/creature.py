import random
from words.service import s

class Somebody: #to love
    def __init__(self, name,
        health  = 100, stamina = 100, mana    = 100,
        attack  = 1,   def_pass= 1,   def_act = 10,  agility = 1, intel=1,
        skills=[], spells=[], mode = 'normal'): #'defend', 'wait'

        self.name       = name

        self.health     = health
        self.stamina    = stamina
        self.mana       = mana

        self.attack     = attack
        self.def_pass   = def_pass
        self.def_act    = def_act
        self.agility    = agility
        self.intel      = intel

        self.skills     = skills
        self.mag_book   = spells

        self.mode       = mode 

        
    def attack_f(self, enemy, damage):
        act, damage = enemy.get_damage(enemy, self.attack)
        return act, enemy.health, damage
    
    def defend_f(self, enemy, damage): 
        self.mode = 'defend'
        return self.mode

    def wait_f(self, enemy, damage):   
        self.mode = 'wait'
        return self.mode

    def get_damage(self, damage):
        if self.mode == 'normal':
            if self.agility >= random.randint(0, 100):
                return 'avoided', 0
            end_damage = damage - self.def_pass

        elif self.mode == 'defend':
            end_damage = damage - self.def_act

        elif self.mode == 'wait':
            end_damage = damage

        self.health -= end_damage
        self.mode = 'normal'
        return 'damaged', end_damage
    
    def list_characteristics(self, s):
        txt = f'{s["health"]}: {self.health}, {s["stamina"]}: {self.stamina}, {s["mana"]}: {self.mana}\n'
        txt+= f'{s["attack"]}: {self.attack}, {s["defence"]}: {self.def_pass}/{self.def_act}\n'
        txt+= f'{s["agility"]}: {self.agility}, {s["intel"]}: {self.intel}\n'
        return txt
    