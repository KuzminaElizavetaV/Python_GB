from HomeWork.Lesson_11.task_1.rectangle import Rectangle

__all__ = ['RectanglePro']


class RectanglePro(Rectangle):
    """
    Расширяет класс Прямоугольник (Rectangle) методами арифметических операций, сравнения и строкового представления
    """
    def __add__(self, other):
        """
        Метод сложения прямоугольников
        """
        sum_perimeters: int = self.get_perimeter() + other.get_perimeter()
        a: int = self.a + other.b
        b: int = sum_perimeters // 2 - a
        return RectanglePro(a, b)

    def __sub__(self, other):
        """
        Метод вычитания прямоугольников
        """
        if self.get_perimeter() < other.get_perimeter():
            self, other = other, self
        diff = self.get_perimeter() - other.get_perimeter()
        a: int = abs(self.a - self.b)
        b: int = diff // 2 - a
        return RectanglePro(a, b)

    def __eq__(self, other):
        """
        Метод сравнения прямоугольников на равенство
        """
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """
        Метод сравнения прямоугольников на больше (>)
        """
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """
        Метод сравнения прямоугольников на меньше или равно (<=)
        """
        return self.get_square() <= other.get_square()

    def __str__(self):
        if self.a != self.b:
            return f'прямоугольник со сторонами {self.a} и {self.b}'
        else:
            return f'квадрат со стороной {self.a}'


if __name__ == '__main__':
    r1 = RectanglePro(3, 2)
    r2 = RectanglePro(5)
    print(r1)
    print(r2)
    print(f'Периметр фигуры {r1} равен {r1.get_perimeter()}')
    print(f'Периметр фигуры {r2} равен {r2.get_perimeter()}')
    rect_sum = r1 + r2
    print(f'Сумма фигур {r1} и {r2} равна {rect_sum.get_perimeter()}')
    print(f'Стороны треугольника после сложения {rect_sum.a} и {rect_sum.b}')
    rect_diff = r1 - r2
    print(f'Разность фигур {r1} и {r2} равна {rect_diff.get_perimeter()}')
    print(f'Стороны треугольника после вычитания {rect_diff.a} и {rect_diff.b}')
    print(f'Проверка на равенство прямоугольника и квадрата => {r1 == r2}')
