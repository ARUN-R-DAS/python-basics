from weapons import AVAILABLE_WEAPONS

class Player():
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.current_weapon = AVAILABLE_WEAPONS['fist']
    
    def __str__(self):
        return (
            f"""
            ===========================
            Health: {self.health}/{self.max_health}
            Current_weapon: {self.current_weapon.name}
            Attack: {self.current_weapon.damage}
            Defence: 0
            ==========================
        """
        )
    
    def take_damage(self, value: int):
        self.health = max(0, self.health - value)
    
    def heal(self, value: int):
        self.health = min(self.max_health, self.health + value)