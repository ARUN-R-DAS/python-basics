class Weapon():
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
    
    def __str__(self):
        return (
            f"""
            Weapon Name: {self.name}
            Damage: {self.damage}
            """
        )