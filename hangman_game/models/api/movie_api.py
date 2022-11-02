from random import randrange
from typing import Union

from models.api.api import Api
from models.utils.movie import Movie
from urlpath import URL


class MovieApi(Api):
    def __init__(self, url: Union[str, URL]):
        super().__init__(url)

    def random_movie(self) -> Movie:
        flag = False
        while flag is False:
            movie = self.__get_random_data()
            if movie["overview"] != "":
                flag = True
        return Movie(movie["title"], movie["overview"])

    def __get_random_data(self) -> Union[dict, None]:
        if self.response.status_code == 200:
            response = self.response.json()
            length = len(response["results"])
            return response["results"][randrange(length)]
        return None
