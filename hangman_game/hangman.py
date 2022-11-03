import os
import sys

SCRIPTS_OPTIONS = ["paises", "estados", "filmes", "manual"]
args = sys.argv

if len(args) >= 2:
    script = args[1].lower()
    if script in SCRIPTS_OPTIONS:
        if script == SCRIPTS_OPTIONS[0]:
            os.system("python automated_hangman_country.py")
        elif script == SCRIPTS_OPTIONS[1]:
            os.system("python automated_hangman_state_of_brazil.py")
        elif script == SCRIPTS_OPTIONS[2]:
            os.system("python automated_hangman_movie.py")
        elif script == SCRIPTS_OPTIONS[3]:
            os.system("python hangman_by_user.py")
    else:
        print(
            f'\nArgumento inválido.\nInsira um valor dentre as opções a seguir: {"/".join(SCRIPTS_OPTIONS)}'
        )
else:
    print(f'\nInsira um valor dentre as opções a seguir: {"/".join(SCRIPTS_OPTIONS)}')
