from random import randrange
from typing import Union

import requests as req
from urlpath import URL


class Api:
    def __init__(self, url: Union[str, URL]):
        self.__url = url
        self.__response = self.__get_url()
        self.__random_data = self.__get_random_data()

    def __get_url(self):
        return req.get(self.__url)

    def __get_random_data(self):
        if self.__response.status_code == 200:
            response = self.__response.json()
            length = len(response)
            return response[randrange(length)]
        return None

    @property
    def random_data(self):
        return self.__random_data
