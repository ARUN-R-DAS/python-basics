import os

from player import Player

player = Player()

 # clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------
def take_input():
    print("--------------------------------------------")
    print("Commands Available:")
    print("1: take 10 damage")
    print("2: heal 5 health")
    print("--------------------------------------------")
    
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
    else:
        print("Invalid input")

    print(player)
#------------------------------------------------------------------
while True:

    i = take_input()

    clear_screen()
    
    handle_game(i)

