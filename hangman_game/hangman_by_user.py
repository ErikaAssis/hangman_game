import sys

from models.hangman import Hangman
from models.utils import cls

args = sys.argv

if len(args) >= 3:
    word = args[1]
    tip = args[2]
else:
    word = str(input("Digite uma palavra: "))
    tip = str(input("Escreva uma dica: "))

cls()

hangman_game = Hangman(word, tip)
hangman_game.start()
