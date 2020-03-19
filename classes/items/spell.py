class Spell:
    def __init__(self, category, abbr, name, descr,
                        attack=0, def_act=0, heal=0, restam=0, cost=0):
        
        self.abbr    = abbr
        self.name    = name 
        self.descr   = descr

        self.attack  = attack
        self.def_act = def_act

        self.heal    = heal
        self.restam  = restam

        self.cost    = cost
        
    def heal_f(self, someone):
        someone.health += self.heal
    
    def restam_f(self, someone):
        someone.stamina += self.restam
    
    def reduce_mana(self, someone):
        someone.mana -= self.cost
    
