import pytest

from hangman_game.models.api.api import Api


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(Api("https://github.com/"), "200")],
)
def test_status_code_200(_class, expected):
    assert _class.response.status_code == int(expected)
