class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.current_weapon = None
    
    def take_damage(self, value: int):
        self.health = max(0, self.health - value)
    
    def heal(self, value: int):
        self.health = min(self.max_health, self.health + value)