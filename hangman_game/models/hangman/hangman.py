class Hangman:
    def __init__(self, word: str, tip: str = None, lives: int = 5):
        self.__word = word.upper().strip()
        self.__lst_word = list(word.upper().strip())
        self.__hangman = self.__secret_word()
        self.__lives = lives
        self.__used_letters = []
        self.__CARACTERS_UNUSED = [""]
        self.__tip = tip.strip()

    def __find_letter(self, letter: str):
        letter = letter
        positions = []
        if ((letter in self.__lst_word) is True) and (len(letter) == 1):
            positions = [i for i, val in enumerate(self.__lst_word) if val == letter]
        return positions

    def __secret_word(self):
        secret_word_lst = []
        for i in self.__lst_word:
            if i == " ":
                secret_word_lst.append(" ")
                continue
            secret_word_lst.append("_")
        return secret_word_lst

    def __check_used_letters(self, letter: str):
        if letter not in self.__used_letters:
            self.__used_letters.append(letter)
            return True
        else:
            return False

    def __hangman_game(self):
        hangman_list = []
        letter = self.__used_letters[-1]
        positions = self.__find_letter(letter)
        if len(positions) == 0:
            self.__lives -= 1
            print(f"A letra {letter} não existe!! Vidas restantes: {self.__lives}")
        else:
            for l in positions:
                self.__hangman[l] = letter

        for i in self.__hangman:
            if i != "_":
                hangman_list.append(i)
                continue
            hangman_list.append("_")

        print(f'-->> {"".join(hangman_list)}\n')
        self.__hangman = hangman_list

    def __winner_message(self):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def __loser_message(self):
        print("#####   GAME OVER   #####")
        print(f"Resposta: {self.__word}")
        print("     _______________        ")
        print("    /               \       ")
        print("   /                 \      ")
        print("/\/                   \/\   ")
        print("\ |   XXXX     XXXX   | /   ")
        print(" \|   XXXX     XXXX   |/    ")
        print("  |   XXX       XXX   |     ")
        print("  |                   |     ")
        print("  \__      XXX      __/     ")
        print("    |\     XXX     /|       ")
        print("    | |           | |       ")
        print("    | I I I I I I I |       ")
        print("    |  I I I I I I  |       ")
        print("    \_             _/       ")
        print("      \_         _/         ")
        print("        \_______/           ")

    def __stop(self):
        if "_" not in "".join(self.__hangman):
            self.__winner_message()
            return True
        elif self.__lives == 0:
            self.__loser_message()
            return True
        return False

    def __read_letter(self):
        caracter_valid = False
        while caracter_valid is False:
            letter = str(input("Digite uma letra: ")).upper().strip()
            if letter in self.__CARACTERS_UNUSED:
                print("Caracter inválido")
            else:
                caracter_valid = True
        return letter

    def start(self):
        stop = False

        print(
            """
            #####################################################################################
            ################################# JOGO DA FORCA #####################################
            #####################################################################################\n"""
        )
        print(f"Palavra possui {len(self.__word)} letras")
        print(f"Você possui {self.__lives} vidas")
        print(f'-->> {"".join(self.__hangman)}\n')

        if (self.__tip is not None) and (len(self.__tip) > 0):
            print(f"Dica: {self.__tip}\n")

        while stop is False:
            letter = self.__read_letter()
            is_new_letter = self.__check_used_letters(letter)
            if is_new_letter is True:
                self.__hangman_game()
                stop = self.__stop()
            else:
                print(f"Letra {letter} já digitada!")
