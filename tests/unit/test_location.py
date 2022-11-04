import pytest

from hangman_game.models.utils.location import Location


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(Location("Brasil", "América do Sul"), "Brasil")],
)
def test_local(_class, expected):
    assert _class.local == expected


@pytest.mark.parametrize(
    ("_class", "expected"),
    [(Location("Brasil", "América do Sul"), "Região América do Sul")],
)
def test_region(_class, expected):
    assert _class.region == expected
