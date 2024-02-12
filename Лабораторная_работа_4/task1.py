"""
Автор: Рябой Евгений
Дата: 12.02.2024
Дисциплина: F-IT (ЦК23-PY2),
Тема:       Итоговое задание
Лабораторная:
            1)
            Выбрать сущности, для которых можно реализовать наследование.
            Например:
                Автомобили — базовый класс. Легковой и грузовой автомобиль — дочерние классы.
                Хвойные деревья — базовый класс. Ель и сосна — дочерние классы.
                Социальные сети — базовый класс. VK, Facebook - дочерние классы.

            2)
            Должны быть реализованы как минимум один базовый и дочерний класс.

            3)
            В базовом классе должны быть реализованы конструктор __init__, магические методы __str__ и __repr__.
            В дочернем классе либо унаследовать, либо расширить конструктор базового класса, унаследовать или
            перегрузить магические методы __str__ и __repr__..

            4)
            Количество атрибутов и методов для каждого класса выбираете самостоятельно.

            5)
            В дочернем классе необходимо унаследовать как минимум один метод и перегрузить один метод
            (помимо магических методов __str__ и __repr__).
            При перегрузке метода обосновать причину, указав её в документации к методу.

            6)
            Если считаете необходимым, то некоторые атрибуты и методы можно сделать непубличными.
            Причину инкапсуляции указать или в виде комментариев для атрибутов или в документации для методов.

            7)
            Все аргументы и выходные результаты методов должны иметь аннотацию типов.

            8)
            Для всех классов и методов должна быть написана документация.
"""

from typing import Union


class StorageDevice:
    """
    Базовый класс, представляющий устройство хранения.

    >>> storage_device = StorageDevice(1024, "SATA")
    >>> storage_device.capacity_gb
    1024
    >>> storage_device.interface
    'SATA'
    """

    def __init__(self, capacity_gb: Union[int, float], interface: str):
        """
        Инициализация объекта устройства хранения.
        :param capacity_gb: Объем устройства хранения в гигабайтах (int или float).
        :param interface: Тип интерфейса устройства хранения (str).

        Атрибуты класса являются защищенными, чтобы ограничить доступ к атрибутам через методы (setter и getter)
        """

        self.capacity_gb = capacity_gb
        self.interface = interface

    @property
    def capacity_gb(self) -> float:
        """
        Получить объем устройства хранения.
        :return: Объем устройства хранения в гигабайтах.
        """
        return self._capacity_gb

    @capacity_gb.setter
    def capacity_gb(self, value: Union[int, float]) -> None:
        """
        Свойство для установки объема устройства хранения.
        :param value: Новое значение объема устройства хранения.
        :raises ValueError: Если value не является положительным числом.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Объем устройства хранения должен быть положительным числом типа int или float.")
        self._capacity_gb = value

    @property
    def interface(self) -> str:
        """
        Получить тип интерфейса устройства хранения.
        :return: Тип интерфейса устройства хранения.
        """
        return self._interface

    @interface.setter
    def interface(self, value: str) -> None:
        """
        Свойство для установки объема устройства хранения.
        :param value: Новое значение типа интерфейса устройства хранения.
        :raises ValueError: Если value не является строковым значением.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("Тип интерфейса устройства хранения должен быть строкой.")
        self._interface = value

    def read_data(self, data_size_gb: Union[int, float]) -> Union[str, None]:
        """
        Симуляция чтения данных с устройства хранения.
        :param data_size_gb: Размер данных для чтения в гигабайтах (float).
        :return: Сообщение о выполнении операции чтения или None, если данных нет.
        """
        if not isinstance(data_size_gb, (int, float)) or data_size_gb <= 0:
            raise ValueError("Размер данных для чтения должен быть положительным числом типа float.")
        if data_size_gb <= self.capacity_gb:
            return f"Чтение {data_size_gb}GB данных с устройства хранения {self.interface}."
        else:
            return None

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта StorageDevice при вызове str().
        :return: Строковое представление устройства хранения.
        """
        return f"Устройство хранения: {self.__class__.__name__}. Объем {self.capacity_gb}GB, Интерфейс {self.interface}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта StorageDevice при вызове repr().
        :return: Формальное строковое представление устройства хранения.
        """
        return f"{self.__class__.__name__}(capacity_gb={self.capacity_gb}, interface={self.interface!r})"


class SSD(StorageDevice):
    """
    Класс, представляющий твердотельный накопитель (SSD).

    >>> ssd = SSD(512, "NVMe")
    >>> ssd.enable_encryption()
    >>> print(ssd)
    Устройство хранения: SSD. Объем 512GB, Интерфейс NVMe, Шифрование True
    >>> repr(ssd)
    "SSD(capacity_gb=512, interface='NVMe', encryption=True)"

    >>> ssd.read_data(100)
    'Расшифровка данных...Чтение 100GB данных с устройства хранения NVMe.'
    """

    def __init__(self, capacity_gb: Union[int, float], interface: str, encryption: bool = False):
        """
        Инициализация объекта SSD.
        :param capacity_gb: Объем SSD в гигабайтах (float).
        :param interface: Тип интерфейса SSD (str).
        :param encryption: Поддержка ли SSD шифрования (по умолчанию False, bool).

        Атрибут класса encryption является защищенным, чтобы ограничить доступ к нему через методы (setter и getter)

        >>> ssd = SSD(256, "SATA")
        >>> ssd.capacity_gb
        256
        """
        super().__init__(capacity_gb, interface)
        self.encryption = encryption

    @property
    def encryption(self) -> bool:
        """
        Получить объем устройства хранения.
        :return: Объем устройства хранения в гигабайтах.
        """
        return self._encryption

    @encryption.setter
    def encryption(self, value: bool) -> None:
        """
        Свойство для установки объема устройства хранения.
        :param value: Новое значение объема устройства хранения.
        :raises ValueError: Если value не логическим типом данных.
        """
        if not isinstance(value, bool):
            raise ValueError("Параметр encryption должен быть типа bool.")
        self._encryption = value

    def enable_encryption(self) -> None:
        """
        Включение шифрования для SSD.
        """
        self.encryption = True

    def read_data(self, data_size_gb: Union[int, float]) -> Union[str, None]:
        """
        Перегруженный метод для чтения данных с SSD.
        Если включено шифрование, выполняются дополнительные проверки безопасности.
        :param data_size_gb: Размер данных для чтения в гигабайтах (float).
        :return: Сообщение о выполнении операции чтения или None, если данных нет.
        """
        if not isinstance(data_size_gb, (int, float)) or data_size_gb <= 0:
            raise ValueError("Размер данных для чтения должен быть положительным числом типа float.")
        if self.encryption:
            return "Расшифровка данных..." + super().read_data(data_size_gb)
        else:
            return super().read_data(data_size_gb)

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для объекта SSD.

        Этот метод переопределен, т.к. дочерний класс расширяет базовый атрибутом encryption

        :return: Строковое представление SSD.
        """
        return f"{super().__str__()}, Шифрование {self.encryption}"

    def __repr__(self) -> str:
        """
        Переопределение метода __repr__ для объекта SSD.

        Этот метод переопределен, т.к. дочерний класс расширяет базовый атрибутом encryption

        :return: Формальное строковое представление устройства хранения.
        """
        return f"{super().__repr__()[:-1]}, encryption={self.encryption})"


class SDCard(StorageDevice):
    """
    Класс, представляющий SD-карту.

    >>> sd_card = SDCard(64, "UHS-I", "Class 10")
    >>> print(sd_card)
    Устройство хранения: SDCard. Объем 64GB, Интерфейс UHS-I, Класс скорости Class 10
    >>> repr(sd_card)
    "SDCard(capacity_gb=64, interface='UHS-I', speed_class='Class 10')"

    >>> sd_card.read_data(20)
    'Чтение 20GB данных с устройства хранения UHS-I.'
    """

    def __init__(self, capacity_gb: Union[int, float], interface: str, speed_class: str):
        """
        Инициализация объекта SD-карты.
        :param capacity_gb: Объем SD-карты в гигабайтах (float).
        :param interface: Тип интерфейса SD-карты (str).
        :param speed_class: Класс скорости SD-карты (например, UHS-I, UHS-II).

        >>> sd_card = SDCard(128, "UHS-II", "Class 20")
        >>> sd_card.speed_class
        'Class 20'
        """
        super().__init__(capacity_gb, interface)
        self.speed_class = speed_class

    @property
    def speed_class(self) -> str:
        """
        Получить класс скорости SD-карты.
        :return: класс скорости SD-карты.
        """
        return self._speed_class

    @speed_class.setter
    def speed_class(self, value: str) -> None:
        """
        Свойство для установки класса скорости SD-карты.
        :param value: Новое значение класса скорости SD-карты.
        :raises ValueError: Если value не строковый тип данных.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("Класс скорости SD-карты должен быть строкой.")
        self._speed_class = value

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для объекта SDCard.

        Этот метод переопределен, т.к. дочерний класс расширяет базовый атрибутом speed_class

        :return: Строковое представление SDCard.
        """
        return f"{super().__str__()}, Класс скорости {self.speed_class}"

    def __repr__(self) -> str:
        """
        Переопределение метода __repr__ для объекта SDCard.

        Этот метод переопределен, т.к. дочерний класс расширяет базовый атрибутом speed_class

        :return: Формальное строковое представление SDCard.
        """
        return f"{super().__repr__()[:-1]}, speed_class={self.speed_class!r})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
