from models.hangman.automated_hangman import AutomatedHangman
from models.utils.location import Localization
from models.api.ibge_api import IBGEApi

url = "https://servicodados.ibge.gov.br/api/v1/localidades/paises"
random_country = IBGEApi(url).random_country()

hangman_game = AutomatedHangman(
    Localization(random_country["country"], random_country["region"])
)
hangman_game.start()
