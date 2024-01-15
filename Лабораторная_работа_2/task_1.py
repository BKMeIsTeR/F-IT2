"""
Автор: Рябой Евгений
Дата: 14.01.2024
Дисциплина: F-IT (ЦК23-PY2),
Тема:       Атрибуты и методы
Лабораторная: Класс Book

Задание:
    1)
    Написать класс Book, конструктор которого будет инициализировать следующие атрибуты:
        id - идентификатор книги
        name - Название книги
        pages - Количество страниц в книге

    2)
    В классе должен быть объявлен метод __str__.
    Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name:

    Книга "название_книги"

    3)
    В классе должен быть объявлен метод __repr__.
    Метод __repr__ должен возвращать валидную python строку, по которой можно инициализировать точно такой же экземпляр.

    Book(id_=1, name='test_name_1', pages=200)
"""

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# Класс представляет книгу с уникальным идентификатором, названием и количеством страниц.
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта класса Book.

        :param id_: Уникальный идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        :raises ValueError: Если id_ не является положительным целым числом или
            pages не является положительным целым числом.
        :raises TypeError: Если name не является строкой.
        """
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("ID должен быть положительным целым числом.")

        if not isinstance(name, str) or not name:
            raise TypeError("Название книги должно быть строкой.")

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Book для отображения при вызове str().

        :return: Строковое представление книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Book для отображения при вызове repr().

        :return: Формальное строковое представление книги.
        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
