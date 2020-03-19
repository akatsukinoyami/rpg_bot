class Item:
    def __init__(self, category, abbr, name, descr,
                        attack=0, def_act=0, def_pass=0, agility=0, intel=0,
                        heal=0, restam=0, remana=0, cost=0):
        
         #skill, spell, head, right_hand, left_hand, cheast, pants, boots, potion, book
        self.category = category 
        self.abbr    = abbr
        self.name    = name 
        self.descr   = descr

        self.attack  = attack
        self.def_act = def_act
        self.def_pass= def_pass
        self.agility = agility
        self.intel   = intel

        self.heal    = heal
        self.restam  = restam
        self.remana  = remana

        self.cost    = cost
        
    def heal_f(self, someone):
        someone.health += self.heal
    
    def restam_f(self, someone):
        someone.stamina += self.restam

    def reduce_stamina(self, someone):
        someone.stamina -= self.cost
    
    def reduce_mana(self, someone):
        someone.mana -= self.cost
    
