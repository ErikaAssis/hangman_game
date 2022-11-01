from models.hangman.hangman import Hangman
from models.utils.location import Localization

class AutomatedHangman(Hangman):
    def __init__(self, localization : Localization):
        super().__init__(localization.local, localization.region)
