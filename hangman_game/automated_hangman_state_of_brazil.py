from models.hangman.automated_hangman import AutomatedHangman
from models.utils.location import Localization
from models.api.ibge_api import IBGEApi
from urlpath import URL

url = URL("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
random_country = IBGEApi(url).random_state_of_brasil()

hangman_game = AutomatedHangman(
    Localization(random_country["state"], random_country["region"])
)
hangman_game.start()
