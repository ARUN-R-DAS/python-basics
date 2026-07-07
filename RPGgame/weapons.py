# weapon database

from weapon import Weapon

FIST = Weapon("Bare Fists", 5)
SWORD = Weapon("Iron Sword", 15)
AXE = Weapon("Battle Axe", 25)
BOW = Weapon("Wooden Box", 10)

AVAILABLE_WEAPONS = {
    "fist": FIST,
    "sword": SWORD,
    "axe": AXE,
    "bow": BOW
}