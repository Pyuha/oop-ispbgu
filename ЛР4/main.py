
class Vegetable:

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f'Имя: {self._name}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r})"


class Tomato(Vegetable):
    def __init__(self, name: str, colour: str, count: int):
        super().__init__(name)
        self.colour = colour
        self.count = count

    def __str__(self) -> str:
        return f"{super().__str__()}, Цвет: {self._colour}, Количество: {self._count}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r}, colour = {self._colour!r}, count = {self._count!r})"

    def how_much_tomatoes(self) -> int:
        return self.count

    @property
    def colour(self) -> str:
        return self._colour

    @property
    def count(self) -> int:
        return self._count

    @colour.setter
    def colour(self, colour: str) -> None:
        if isinstance(colour, str) == True:
            self._colour = colour
        else:
            raise TypeError('Неверный формат, необходим строчный формат')

    @count.setter
    def count(self, count: int) -> None:
        if isinstance(count, int):
            if count > 0:
                self._count = count
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')


class Carrot(Vegetable):
    def __init__(self, name: str, colour: str, long: int):
        super().__init__(name)
        self.colour = colour
        self.long = long

    def __str__(self) -> str:
        return f"{super().__str__()}, Цвет: {self._colour}, Длина: {self._long}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self._name!r}, colour = {self._colour!r}, long = {self._long!r})"

    def how_long_carrot(self) -> int:
        return self.long

    @property
    def colour(self) -> str:
        return self._colour

    @property
    def long(self) -> int:
        return self._long

    @colour.setter
    def colour(self, colour: str) -> None:
        if isinstance(colour, str) == True:
            self._colour = colour
        else:
            raise TypeError('Неверный формат, необходим строчный формат')

    @long.setter
    def count(self, long: int) -> None:
        if isinstance(long, int):
            if long > 0:
                self._long = long
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')