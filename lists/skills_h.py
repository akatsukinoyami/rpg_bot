from classes.item     import Item

class SkillsH:
    def __init__(self):
        self.kick   = Item('skill', 'kick', 'Удар ногой', 'Отмашистый удар ногой', 
                            attack=5, cost=10)
        self.beat   = Item('skill', 'beat', 'Удар кулаком', 'Не сильный удар', 
                            attack=3, cost=5)
        self.remana = Item('skill', 'remana','Медитация', 'Восстанавливает ману', 
                            remana=5, cost=7)