from player import Player

player = Player()

while True:
    print("--------------------------------------------")
    print("Commands Available:")
    print("1: take 10 damage")
    print("2: heal 5 health")
    
    try:
        i = int(input("input: "))
    except:
        print(">>>>>>>>>>>>>>>Invalid Input")
        continue
    print("--------------------------------------------")
    if i == 1:
        player.take_damage(10)
        print("Player took 10 damage")
    elif i == 2:
        player.heal(5)
        print("Player healed 5 health")

    print(f"Player Health: {player.health}")

