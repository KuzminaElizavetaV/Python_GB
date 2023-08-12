__all__ = ['Restangle']


class Restangle:
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

    def get_perim(self):
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
    r1 = Restangle(3, 2)
    r2 = Restangle(5)
    print(r1.get_perim())
    print(r1.get_square())
    print(r2.get_perim())
    print(r2.get_square())
