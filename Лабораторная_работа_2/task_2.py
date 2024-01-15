"""
Автор: Рябой Евгений
Дата: 14.01.2024
Дисциплина: F-IT (ЦК23-PY2),
Тема:       Атрибуты и методы
Лабораторная: Класс Library

Задание:
    1)
    Написать класс Library, конструктор которого будет инициализировать следующие атрибуты:
        books - Список книг

    Конструктор должен принимать необязательный аргумент со значением по умолчанию.
    Если пользователь его не передал, то библиотека инициализируется с пустым списком книг.

    2)
    В классе должен быть объявлен метод get_next_book_id.
    Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.

    3)
    В классе должен быть объявлен метод get_index_by_book_id.
    Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
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


# Класс представляет библиотеку с списком книг.
class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация объекта класса Library.

        :param books: Список книг для инициализации библиотеки.
            По умолчанию - пустой список.
        """
        if books is None:
            books = []
        elif not isinstance(books, list):
            raise TypeError("Параметр 'books' должен быть списком книг.")

        self.books = books

    def get_next_book_id(self) -> int:
        """
        Получение следующего уникального идентификатора для новой книги.

        :return: Следующий уникальный идентификатор.
        """
        if not self.books:
            return 1

        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Получение индекса книги по её уникальному идентификатору.

        :param book_id: Уникальный идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с указанным идентификатором не существует.
        :raises TypeError: Если book_id не положительное целое число.
        """
        if not isinstance(book_id, int) or book_id <= 0:
            raise TypeError("book_id должен быть положительным целым числом")

        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i

        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
