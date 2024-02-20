class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self) -> str:
        return f"{super().__str__()}. Число страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if isinstance(self.pages, int):
            if pages > 0:
                self._pages = pages
            else:
                raise TypeError("Неверный формат данных, он не может быть отрицательным или равен нулю.")
        else:
            raise TypeError('Неверный формат данных, он должен быть целочисленного типа.')


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if isinstance(self.duration, float):
            if duration > 0:
                self._duration = duration
            else:
                raise TypeError("Неверный формат данных, он не может быть отрицательным или равен нулю.")
        else:
            raise TypeError('Неверный формат данных, он должен быть вещественного типа')
