class Localization:
    def __init__(self, local: str, region: str):
        self.__local = local
        self.__region = region

    @property
    def local(self) -> str:
        return self.__local

    @property
    def region(self) -> str:
        return f"Região {self.__region}"
