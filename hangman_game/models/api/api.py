from typing import Union

import requests as req
from urlpath import URL


class Api:
    def __init__(self, url: Union[str, URL]):
        self.__url = url
        self.__response = self.__get_url()

    def __get_url(self):
        return req.get(self.__url)

    @property
    def response(self):
        return self.__response
