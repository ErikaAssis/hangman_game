from models import Hangman, IBGEApi

url = "https://servicodados.ibge.gov.br/api/v1/localidades/paises"
random_country = IBGEApi(url).random_country()

hangman_game = Hangman(random_country.local, random_country.region)
hangman_game.start()
