class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration} часов"

if __name__ == '__main__':
    """ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ """

    # Создание объекта базового класса Book
    book = Book(name="Имя книги", author="Автор")
    print(book)  # Вывод: Книга Имя книги. Автор Автор

    # Создание объекта класса PaperBook
    paper_book = PaperBook(name="Бумажная книга", author="Автор бумажной книги", pages=200)
    print(paper_book)  # Вывод: Книга Бумажная книга. Автор Автор бумажной книги Количество страниц: 200

    # Изменение количества страниц бумажной книги через свойство
    paper_book.pages = 250
    print(paper_book)  # Вывод: Книга Бумажная книга. Автор Автор бумажной книги Количество страниц: 250

    # Создание объекта класса AudioBook
    audio_book = AudioBook(name="Аудиокнига", author="Автор аудиокниги", duration=8.5)
    print(audio_book)  # Вывод: Книга Аудиокнига. Автор Автор аудиокниги Продолжительность: 8.5 часов

    # Изменение продолжительности аудиокниги через свойство
    audio_book.duration = 10.2
    print(audio_book)  # Вывод: Книга Аудиокнига. Автор Автор аудиокниги Продолжительность: 10.2 часов