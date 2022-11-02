from models.api.ibge_api import IBGEApi
from models.hangman.hangman import Hangman
from urlpath import URL

url = URL("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
random_state = IBGEApi(url).random_state_of_brasil()

hangman_game = Hangman(random_state.local, random_state.region)
hangman_game.start()
