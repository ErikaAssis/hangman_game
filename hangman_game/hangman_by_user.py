from models.hangman.hangman import Hangman
from models.utils.utils import cls

word = str(input("Digite uma palavra: "))
tip = str(input("Escreva uma dica: "))

cls()

hangman_game = Hangman(word, tip)
hangman_game.start()
