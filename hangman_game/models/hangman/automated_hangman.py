from models.hangman.hangman import Hangman
from models.utils.location import Localization

from math import ceil


class AutomatedHangman(Hangman):
    def __init__(self, localization: Localization):
        lives = self.__hit_attempts(localization.local)
        super().__init__(localization.local, localization.region, lives)

    def __hit_attempts(self, word):
        return ceil(len(word) / 2)
