from typing import Union

from models.api.api import Api
from models.utils.location import Localization
from urlpath import URL


class IBGEApi(Api):
    def __init__(self, url: Union[str, URL]):
        super().__init__(url)

    def random_state_of_brasil(self):
        state = self.random_data
        return Localization(state["nome"], state["regiao"]["nome"])

    def random_country(self):
        country = self.random_data
        return Localization(country["nome"], country["sub-regiao"]["nome"])
