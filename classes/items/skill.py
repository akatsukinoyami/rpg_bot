class Skill:
    def __init__(self, category, abbr, name, descr,
                        attack=0, def_act=0, remana=0, cost=0):
        
        self.abbr    = abbr
        self.name    = name 
        self.descr   = descr

        self.attack  = attack
        self.def_act = def_act

        self.remana  = remana

        self.cost    = cost

    def reduce_stamina(self, someone):
        someone.stamina -= self.cost