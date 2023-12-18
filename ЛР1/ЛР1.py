import doctest


class Button:
    def __init__(self, colour: str, assign: str):
        """
        Создание объекта "Кнопка"

        :param colour: Цвет кнопки
        :param assign: Назначение кнопки

        Примеры:
        >>> button1 = Button('Зеленая', 'Включение')
        >>> button2 = Button('Красная', 'Выключение')
        """
        self.colour = colour
        self.assign = assign

    def enable_button(self):
        """
        Включение кнопки
        """
    def turn_off_button(self):
        """
        Выключение кнопки
        """
    def reassign_button(self, assign):
        """
        Переназначение кнопки
        """


class Book:
    def __init__(self, title: str, subject: str):
        """
        Создание объекта "Книга"

        :param title: Название книги
        :param subject: Предмет книги

        Примеры:
        >>> book1 = Book('Роме и Джульетта', 'Пьеса')
        >>> book2 = Book('Алгебра простым языком', 'Учебник')
        """
        self.title = title
        self.subject = subject

    def take_a_book(self):
        """
        Взять книгу
        """
    def put_the_book_away(self):
        """
        Отдать книгу
        """


class Product:
    def __init__(self, price: float, title: str):
        """
        Создание объекта "Товар"

        :param price: Цена товара
        :param title: Название товара

        Примеры:
        >>> product1 = Product(250.5, 'Колбаса')
        >>> product2 = Product(40.2, 'Минеральная вода')
        """
        self.price = price
        self.title = title

    def buy_a_product(self):
        """
        Купить товар
        """
    def return_product(self):
        """
        Вернуть товар
        """


if __name__ == "__main__":
    doctest.testmod()
