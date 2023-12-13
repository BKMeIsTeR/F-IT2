"""
Автор: Рябой Евгений
Дата: 12.12.2023
Дисциплина: F-IT (ЦК23-PY2),
Тема:       Основы ООП
Лабораторная: Придумать и написать 3 абстрактных класса, описывающих любой объект.
"""


class MusicPlayer:
    def __init__(self, volume: int = 50, playlist: list[str] = None):
        """
        Создает объект класса MusicPlayer.

        :param volume: Уровень громкости плеера (от 0 до 100). По умолчанию 50.
        :param playlist: Список композиций в плейлисте. По умолчанию None.
        :raise ValueError: Если уровень громкости не в диапазоне (от 0 до 100),то возвращается ошибка.

        >>> player1 = MusicPlayer(50, ["1", "2"])  # инициализация экземпляра класса
        >>> player2 = MusicPlayer(50)  # инициализация экземпляра класса
        >>> player1.volume
        50
        >>> player1.playlist
        ['1', '2']
        >>> player2.volume
        50
        >>> player2.playlist
        []
        """
        if not isinstance(volume, int) or volume < 0 or volume > 100:
            raise TypeError("volume должен быть целым числом от 0 до 100")

        if playlist is None:
            playlist = []  # Если playlist не был передан, устанавливаем пустой список
        else:
            # Проверяем, что playlist является списком
            if not isinstance(playlist, list):
                raise TypeError("Playlist должен быть типом list")
            # Проверяем, что playlist является списком со строковыми элементами
            if not all(isinstance(song, str) for song in playlist):
                raise ValueError("Playlist должен быть списком со строковыми элементами")

        self.volume = volume
        self.playlist = playlist

    def play_song(self, song: str) -> None:
        """
        Воспроизводит указанную композицию из плейлиста.

        :param song: Название композиции.
        :raise ValueError: Если композиция пустая строка,то возвращается ошибка.
        """
        if not isinstance(song, str) or not song:
            raise ValueError("Композиция должна быть непустой строкой")
        ...

    def add_to_playlist(self, song: str) -> None:
        """
        Добавляет композицию в плейлист.

        :param song: Название композиции для добавления.
        :raise ValueError: Если композиция пустая строка,то возвращается ошибка.
        """
        if not isinstance(song, str) or not song:
            raise ValueError("Композиция должна быть непустой строкой")
        ...

    def change_volume(self, volume_level: int) -> None:
        """
        Изменяет уровень громкости.

        :param volume_level: Новый уровень громкости (от 0 до 100).
        :raise ValueError: Если новый уровень громкости не в диапазоне (от 0 до 100),то возвращается ошибка.
        """
        if not isinstance(volume_level, int) or volume_level < 0 or volume_level > 100:
            raise TypeError("volume должен быть целым числом от 0 до 100")
        ...


class SocialNetworkUser:
    def __init__(self, username: str, age: int, email: str):
        """
        Создает объект класса SocialNetworkUser.

        :param username: Имя пользователя.
        :param age: Возраст пользователя.
        :param email: Email пользователя.
        :raise ValueError: Если username пустая строка или
                        возраст меньше 1 года или
                        email имеент некорректный формат,то возвращается ошибка.

        >>> user = SocialNetworkUser('Popkov Ivan', 25, 'popkov@example.com')
        >>> user.username
        'Popkov Ivan'
        >>> user.age
        25
        >>> user.email
        'popkov@example.com'
        >>> user.friends
        []
        >>> user.friends_count
        0
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Имя пользователя должно быть непустой строкой")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        if not isinstance(email, str) or not email.count("@") == 1:
            raise ValueError("Некорректный формат email")

        self.username = username
        self.age = age
        self.email = email

        self.friends = []
        self.friends_count = 0

    def send_message(self, user: 'SocialNetworkUser', message: str) -> None:
        """
        Отправляет сообщение другому пользователю.

        :param user: Пользователь, которому отправляется сообщение.
        :param message: Текст сообщения.
        :raise ValueError: Если user не экземпляр класса SocialNetworkUser или
                        message пустая строка,то возвращается ошибка.
        """
        if not isinstance(user, SocialNetworkUser):
            raise ValueError("Аргумент 'user' должен быть экземпляром класса SocialNetworkUser")
        if not isinstance(message, str) or not message:
            raise ValueError("Сообщение должно быть непустой строкой")
        ...

    def add_friend(self, user: 'SocialNetworkUser') -> None:
        """
        Добавляет пользователя в список друзей.

        :param user: Пользователь, которого нужно добавить в друзья.
        :raise ValueError: Если user не экземпляр класса SocialNetworkUser,то возвращается ошибка.
        """
        if not isinstance(user, SocialNetworkUser):
            raise ValueError("Аргумент 'user' должен быть экземпляром класса SocialNetworkUser")
        ...

    def remove_friend(self, user: 'SocialNetworkUser') -> None:
        """
        Удаляет пользователя из списка друзей.

        :param user: Пользователь, которого нужно удалить из друзей.
        :raise ValueError: Если user не экземпляр класса SocialNetworkUser,то возвращается ошибка.
        """
        if not isinstance(user, SocialNetworkUser):
            raise ValueError("Аргумент 'user' должен быть экземпляром класса SocialNetworkUser")
        ...


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Создает объект класса BankAccount.

        :param account_number: Номер банковского счета.
        :param balance: Баланс банковского счета
        :raise ValueError: Если номер банковского счета пустая строка или
                        баланс банковского счета меньше 0.0,то возвращается ошибка.

        >>> account = BankAccount('1234567890', 1457.54)
        >>> account.account_number
        '1234567890'
        >>> account.balance
        1457.54
        """
        if not isinstance(account_number, str) or not account_number:
            raise ValueError("Номер банковского счета должен быть непустой строкой")
        if not isinstance(balance, (int, float)) or balance < 0.0:
            raise ValueError("Баланс банковского счета должен быть числом от 0.0")

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополняет счет на указанную сумму.

        :param amount: Сумма для пополнения.
        :raise ValueError: Если сумма для снятия не положительное число,то возвращается ошибка.
        """
        if not isinstance(amount, (int, float)) or amount <= 0.0:
            raise ValueError("Сумма для пополнения должна быть положительным числом")
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снимает указанную сумму со счета.

        :param amount: Сумма для снятия.
        :raise ValueError: Если сумма для снятия не положительное число,то возвращается ошибка.
        """
        if not isinstance(amount, (int, float)) or amount <= 0.0:
            raise ValueError("Сумма для снятия должна быть положительным числом")
        ...

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс на счете.

        :return: Текущий баланс на счете.
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
