#HANGMAN Project

# import os
import random
import config
from ascii import logo, stages

# def game_menu(state):
#     clear()
#     if state == 0:
#         print(logo)
#         print("Welcome to CUM ZONE")
#     elif state == 1:
#         print("Win!")
#     elif state == 2:
#         print("Game over..")
#     if input("Press Enter to start new game ") == "" :
#         gameplay()
#     else:
#         print("Game closed")
#         exit(0)

def gameplay():
    print(logo)
    print("Welcome to CUM ZONE")

    stats = config.stats()
    while(stats.health != 0):
        correct = False
        key = input("Enter word: ")
        for index, letter in enumerate(stats.wordline):
            if key == letter:
                correct = True
                stats.wordboard[index] = stats.wordline[index]
        if correct == False : stats.health -= 1
        word_display(stats)
        if stats.health == 0:
            print("You lose. The ungessed word was", "".join(stats.wordline).upper())
            exit(0)
        if "_" not in stats.wordboard:
            print("You win")
            exit(0)

def word_display(stats):
    print(stages[stats.health])
    print("You have ", stats.health, " tries" if stats.health != 1 else " try")
    print(''.join(stats.wordboard).upper())

gameplay()