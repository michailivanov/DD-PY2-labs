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

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


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

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

if __name__ == '__main__':
    """ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ """

    # Создание экземпляра класса Book
    book1 = Book(name="Гарри Поттер и философский камень", author="Джоан Роулинг")

    # Вывод строки с использованием __str__
    print(str(book1))  # Вывод: Книга Гарри Поттер и философский камень. Автор Джоан Роулинг

    # Вывод строки с использованием __repr__
    print(repr(book1))  # Вывод: Book(name='Гарри Поттер и философский камень', author='Джоан Роулинг')

    # Создание экземпляра класса PaperBook
    paper_book = PaperBook(name="Три товарища", author="Эрих Мария Ремарк", pages=400)

    # Вывод строки с использованием __str__
    print(str(paper_book))  # Вывод: Книга Три товарища. Автор Эрих Мария Ремарк

    # Вывод строки с использованием __repr__
    print(repr(paper_book))  # Вывод: PaperBook(name='Три товарища', author='Эрих Мария Ремарк', pages=400)

    # Создание экземпляра класса AudioBook
    audio_book = AudioBook(name="1984", author="Джордж Оруэлл", duration=8.5)

    # Вывод строки с использованием __str__
    print(str(audio_book))  # Вывод: Книга 1984. Автор Джордж Оруэлл

    # Вывод строки с использованием __repr__
    print(repr(audio_book))  # Вывод: AudioBook(name='1984', author='Джордж Оруэлл', duration=8.5)
