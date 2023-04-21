import os

def game_menu(state):
    if state == 0:
        print("Welcome to CUM ZONE")
    elif state == 1:
        print("Lose")
    elif state == 2:
        print("Lose")

    os.system('cls' if os.name == 'nt' else 'clear')

    if input("Press Enter to start new game ") == "" :
        start_game()
    else:
        print("Game closed")
        exit(1)