import requests as req
from random import randrange
from urlpath import URL
from typing import Union

from models.api.api import Api


class IBGEApi(Api):
    def __init__(self, url: Union[str, URL]):
        super().__init__(url)

    def random_state_of_brasil(self):
        state = self.random_data
        return {"state": state["nome"], "region": state["regiao"]["nome"]}

    def random_country(self):
        country = self.random_data
        return {"country": country["nome"], "region": country["sub-regiao"]["nome"]}
