import pytest

from hangman_game.models.api.movie_api import MovieApi
from hangman_game.models.utils.movie import Movie

URL = "https://api.themoviedb.org/3/movie/popular?api_key=6f7cad428d6255687d23f8a8907d2d53&language=pt-BR"


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(MovieApi(URL), Movie)],
)
def test_random_movie(_class, expected):
    assert isinstance(_class.random_movie(), expected)
