import pytest

from hangman_game.models.api.ibge_api import IBGEApi
from hangman_game.models.utils.location import Location

URL_STATES = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
URL_COUNTRY = "https://servicodados.ibge.gov.br/api/v1/localidades/paises"


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(IBGEApi(URL_STATES), Location)],
)
def test_random_state_of_brasil(_class, expected):
    assert isinstance(_class.random_state_of_brasil(), expected)


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(IBGEApi(URL_COUNTRY), Location)],
)
def test_random_country(_class, expected):
    assert isinstance(_class.random_country(), expected)
