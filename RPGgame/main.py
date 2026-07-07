from .player import Player

player = Player()

while True:
    print("Commands Available:")
    print("1: take 10 damage")
    print("2: heal 5 health")
    try:
        input = int("Input: ")
    except:
        print("Invalid input")
    
    match input:
        case 1:
            player.take_damage(10)
        case 2:
            player.heal(10)