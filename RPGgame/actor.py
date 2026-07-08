from weapons import AVAILABLE_WEAPONS

class Actor():
    def __init__(self, name, x, y, health, max_health):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.current_weapon = AVAILABLE_WEAPONS['fist']

        self.x = x
        self.y = y
    
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