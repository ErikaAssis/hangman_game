import pytest

from hangman_game.models.utils.movie import Movie


@pytest.mark.parametrize(
    ("_class", "expected"),
    [
        (
            Movie(
                "Code Name Banshee",
                "Caleb � um ex-assassino do governo vivendo escondido. Ele ressurge quando sua protegida, a assassina igualmente mortal conhecida como Banshee, descobre que h� uma recompensa pela cabe�a de Caleb.",
            ),
            "Code Name Banshee",
        )
    ],
)
def test_title(_class, expected):
    assert _class.title == expected


@pytest.mark.parametrize(
    ("_class", "expected"),
    [
        (
            Movie(
                "Code Name Banshee",
                "Caleb é um ex-assassino do governo vivendo escondido. Ele ressurge quando sua protegida, a assassina igualmente mortal conhecida como Banshee, descobre que há uma recompensa pela cabeça de Caleb.",
            ),
            "Caleb é um ex-assassino do governo vivendo escondido. Ele ressurge quando sua protegida, a assassina igualmente mortal conhecida como Banshee, descobre que há uma recompensa pela cabeça de Caleb.",
        )
    ],
)
def test_overview(_class, expected):
    assert _class.overview == expected
