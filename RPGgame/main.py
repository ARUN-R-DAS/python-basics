import os

from player import Player
from weapons import AVAILABLE_WEAPONS

player = Player()

#------------------------------------------------------------------
def take_input():
    print("""
    --------------------------------------------
    Commands Available:
    1: take 10 damage
    2: heal 5 health
    3: Equip Sword
    4: Sheath Sword
    --------------------------------------------
    """)
    try:
        i = int(input("input: "))
    except:
        i = None

    print("--------------------------------------------")

    return i
#------------------------------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------
def handle_game(i):
    if i == 1:
        player.take_damage(10)
        print("Player took 10 damage")
    elif i == 2:
        player.heal(5)
        print("Player healed 5 health")
    elif i == 3:
        player.current_weapon = AVAILABLE_WEAPONS["sword"]
    elif i == 4:
        player.current_weapon = AVAILABLE_WEAPONS["fist"]
    else:
        print("Invalid input")

    print(player)
#------------------------------------------------------------------
clear_screen()
while True:

    i = take_input()

    clear_screen()
    
    handle_game(i)

