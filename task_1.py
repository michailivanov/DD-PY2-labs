import doctest
from typing import List


# Написать 3 класса с документацией и аннотацией типов
class Car:
    """
    Абстрактный класс, описывающий машину.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация объекта машины.

        :param brand: Марка машины.
        :param model: Модель машины.
        :param year: Год выпуска машины.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        """
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год выпуска должен быть положительным целым числом.")
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Абстрактный метод, описывающий запуск двигателя машины.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.start_engine()
        """
        pass

    def drive(self, destination: str, speed: float) -> None:
        """
        Абстрактный метод, описывающий движение машины.

        :param destination: Место, куда направляется машина.
        :param speed: Скорость движения машины.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.drive("City Center", 60.0)
        """
        pass

    def stop_engine(self) -> None:
        """
        Абстрактный метод, описывающий остановку двигателя машины.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.stop_engine()
        """
        pass


class Animal:
    """
    Абстрактный класс, описывающий животное.
    """

    def __init__(self, species: str, habitat: str, sound: str):
        """
        Инициализация объекта животного.

        :param species: Вид животного.
        :param habitat: Среда обитания животного.
        :param sound: Звук, издаваемый животным.

        Примеры:
        >>> lion = Animal("Lion", "Grasslands", "Roar")
        """
        self.species = species
        self.habitat = habitat
        self.sound = sound

    def move(self, destination: str) -> None:
        """
        Абстрактный метод, описывающий перемещение животного.

        :param destination: Место, куда направляется животное.

        Примеры:
        >>> lion = Animal("Lion", "Grasslands", "Roar")
        >>> lion.move("Watering Hole")
        """
        pass

    def make_sound(self) -> None:
        """
        Абстрактный метод, описывающий издачу звука животным.

        Примеры:
        >>> lion = Animal("Lion", "Grasslands", "Roar")
        >>> lion.make_sound()
        """
        pass

    def sleep(self) -> None:
        """
        Абстрактный метод, описывающий сон животного.

        Примеры:
        >>> lion = Animal("Lion", "Grasslands", "Roar")
        >>> lion.sleep()
        """
        pass


class SocialNetwork:
    """
    Абстрактный класс, описывающий социальную сеть.
    """

    def __init__(self, name: str, users: List[str]):
        """
        Инициализация объекта социальной сети.

        :param name: Название социальной сети.
        :param users: Список пользователей в сети.

        Примеры:
        >>> telegram = SocialNetwork("Telegram", ["Web Wizard", "Internet Guru", "Super Tech"])
        """
        self.name = name
        self.users = users

    def create_post(self, user: str, content: str) -> None:
        """
        Абстрактный метод, описывающий создание поста пользователем.

        :param user: Пользователь, создающий пост.
        :param content: Содержание поста.


        Примеры:
        >>> telegram = SocialNetwork("Telegram", ["Web Wizard", "Internet Guru", "Super Tech"])
        >>> telegram.create_post("Super Tech", "Hello, World!")
        """
        pass

    def add_friend(self, user: str, friend: str) -> None:
        """
        Абстрактный метод, описывающий добавление друга в сети.

        :param user: Пользователь, добавляющий друга.
        :param friend: Пользователь, который становится другом.

        Примеры:
        >>> telegram = SocialNetwork("Telegram", ["Web Wizard", "Internet Guru", "Super Tech"])
        >>> telegram.add_friend("Web Wizard", "Internet Guru")
        """
        pass

    def get_user_posts(self, user: str) -> List[str]:
        """
        Абстрактный метод, возвращающий посты пользователя.

        :param user: Пользователь, чьи посты необходимо получить.
        :return: Список постов пользователя.

        Примеры:
        >>> telegram = SocialNetwork("Telegram", ["Web Wizard", "Internet Guru", "Super Tech"])
        >>> telegram.get_user_posts("Internet Guru")
        """
        pass


if __name__ == "__main__":
    # работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
