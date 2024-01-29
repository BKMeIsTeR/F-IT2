"""
Автор: Рябой Евгений
Дата: 25.01.2024
Дисциплина: F-IT (ЦК23-PY2),
Тема:       Инкапсуляция, наследование и полиморфизм
Лабораторная: Классы PaperBook и AudioBook
Задание:
    Есть два типа книг - бумажная и аудио.
    Для всех типов хранения книг у них есть: - название (name) - автор (author)

    У бумажной книги есть количество страниц (pages) целочисленного типа данных. У аудио книги есть её
    продолжительность (duration) как числа с плавающей запятой.

    1)
    Для классов Book, PaperBook, AudioBook примените наследование.
    2)
    Исходя из кода подумайте когда методы __str__ и __repr__ могут быть унаследованы, а когда перегружены в
    дочерних классах. И исправьте это
    3)
    Атрибуты name и author изменяться не могут, поэтому напишите для них свойства, которые не
    позволят изменять эти атрибуты.
    4)
    Так как на pages и duration накладываются ограничения по типу и допустимым значениям, напишите для них свойства с
     проверками при присвоении им значений.
"""


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация объекта класса Book.
        :param name: Название книги.
        :param author: Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """
        Свойство для получения названия книги.
        :return: Название книги.
        """
        return self._name

    @property
    def author(self):
        """
        Свойство для получения автора книги.
        :return: Автор книги.
        """
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление объекта Book при вызове str().
        :return: Строковое представление книги.
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта Book при вызове repr().
        :return: Формальное строковое представление книги.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Класс представляет бумажную книгу.
    """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта класса PaperBook.
        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        """
        Свойство для получения количества страниц в книге.
        :return: Количество страниц.
        """
        return self._pages

    @pages.setter
    def pages(self, value):
        """
        Свойство для установки количества страниц в книге.
        :param value: Новое значение количества страниц.
        :raises ValueError: Если value не является положительным целым числом.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом.")
        self._pages = value

    def __str__(self):
        """
        Возвращает строковое представление объекта PaperBook при вызове str().
        :return: Строковое представление бумажной книги.
        """
        return f"{super().__str__()}. Количество страниц {self.pages}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта PaperBook при вызове repr().
        :return: Формальное строковое представление бумажной книги.
        """
        return f"{super().__repr__()}, pages={self.pages})"


class AudioBook(Book):
    """
    Класс представляет аудиокнигу.
    """

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация объекта класса AudioBook.
        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Длительность аудиокниги в часах.
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        """
        Свойство для получения длительности аудиокниги.
        :return: Длительность аудиокниги в часах.
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """
        Свойство для установки длительности аудиокниги.
        :param value: Новое значение длительности.
        :raises ValueError: Если value не является положительным числом.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        """
        Возвращает строковое представление объекта AudioBook при вызове str().
        :return: Строковое представление аудиокниги.
        """
        return f"{super().__str__()}. Длительность {self.duration}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта AudioBook при вызове repr().
        :return: Формальное строковое представление аудиокниги.
        """
        return f"{super().__repr__()}, duration={self.duration})"


# Пример создания объектов PaperBook и AudioBook.
paper_book = PaperBook("Черный обелиск", "Эрих Мария Ремарк", 416)
audio_book = AudioBook("Братья Карамазовы", "Достоевский Ф.М.", 51.22)

# Вывод информации о книгах.
print(paper_book)
print(repr(paper_book))
print(audio_book)
print(repr(audio_book))
