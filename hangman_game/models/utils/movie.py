class Movie:
    def __init__(self, title: str, overview: str):
        self.__title = title.strip()
        self.__overview = overview.strip()

    @property
    def title(self) -> str:
        return self.__title

    @property
    def overview(self) -> str:
        return self.__overview
