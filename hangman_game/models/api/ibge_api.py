from random import randrange
from typing import Union

from urlpath import URL

from hangman_game.models.api.api import Api
from hangman_game.models.utils.location import Location


class IBGEApi(Api):
    def __init__(self, url: Union[str, URL]):
        super().__init__(url)

    def random_state_of_brasil(self) -> Location:
        state = self.__get_random_data()
        return Location(state["nome"], state["regiao"]["nome"])

    def random_country(self) -> Location:
        country = self.__get_random_data()
        return Location(country["nome"], country["sub-regiao"]["nome"])

    def __get_random_data(self) -> Union[dict, None]:
        if self.response.status_code == 200:
            response = self.response.json()
            length = len(response)
            return response[randrange(length)]
        return None
