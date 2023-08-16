__all__ = ['Rectangle']


class Rectangle:
    """
    Класс реализует объект Прямоугольник
    """
    def __init__(self, a: int, b: int = None):
        """
        Инициализация объекта прямоугольник со сторонами a, b
        :param a: длина
        :param b: ширина
        """
        self.a = a
        if not b:
            self.b = a
        else:
            self.b = b

    def get_perimeter(self):
        """
        Метод возвращает периметр прямоугольника
        """
        return 2 * (self.a + self.b)

    def get_square(self):
        """
        Метод возвращает площадь прямоугольника
        """
        return self.a * self.b


if __name__ == '__main__':
    r1 = Rectangle(3, 2)
    r2 = Rectangle(5)
    print(r1.get_perimeter())
    print(r1.get_square())
    print(r2.get_perimeter())
    print(r2.get_square())
