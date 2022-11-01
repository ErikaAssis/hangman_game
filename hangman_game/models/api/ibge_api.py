import requests as req
from random import randrange
from urlpath import URL
from typing import Union


class IBGEApi:
    def __init__(self, url: Union[str, URL]):
        self.__url = url
        self.__response = self.__get_url()

    def __get_url(self):
        return req.get(self.__url)

    def __get_data(self):
        if self.__response.status_code == 200:
            response = self.__response.json()
            length = len(response)
            return response[randrange(length)]

    def random_state_of_brasil(self):
        state = self.__get_data()
        return {"state": state["nome"], "region": state["regiao"]["nome"]}

    def random_country(self):
        country = state = self.__get_data()
        return {"country": country["nome"], "region": country["sub-regiao"]["nome"]}
