def run():
    print("STATE A active")

    choice = input("Do you want to switch into state c (y/n)")
    print('choice: ',choice)
    if choice == 'y':
        print("y picked, returning 2")
        return 2
    
    return None