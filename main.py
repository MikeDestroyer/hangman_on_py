#HANGMAN Project

import random
import menu

words = ["Hello", "World", "lorem", "Minecraft"]
word = []

def gererate_wrodline(word_list):
    word = random.choice(word_list).lower()
    word_line = []
    for letter in word:
        word_line += [letter]
    return word_line


menu.game_menu(0)

def gameplay():
    health = 6
    wordline = gererate_wrodline(words)
    while(life != 0):
        key = input("Enter word: ")
        correct = false
        for letter in wordline:
            if key == letter:
                print("correct")
                correct = true
            else:
                print("uncorrect")






