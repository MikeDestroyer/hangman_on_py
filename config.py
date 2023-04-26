
import random
class stats:
    def gererate_wrodline(word_list):
        word = random.choice(word_list).lower()
        word_line = []
        for letter in word:
            word_line += [letter]
        return word_line

    def generate_board(wordline):
        board = []
        for index in enumerate(wordline):
            board += ["_"]
        return board

    health = 6
    words = ["Hello", "World", "lorem", "Minecraft"]
    wordline = gererate_wrodline(words)
    wordboard = generate_board(wordline)
