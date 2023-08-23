class Matrix:
    """
    В классе реализован функционал сравнения прямоугольных матриц, а также возможность производить арифметические
    действия над ними
    """
    def __init__(self, matrix: list[list[int]]):
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину!")
        self.matrix = matrix

    def __str__(self):
        """
        Метод представления матрицы в виде строки
        """
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        """
        Метод сложения матриц
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для выполнения операции сложение размеры матриц должны совпадать!")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __sub__(self, other):
        """
        Метод вычитания матриц
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для выполнения операции вычитание размеры матриц должны совпадать!")
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        """
        Метод умножения матриц
        """
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __eq__(self, other):
        """
        Метод проверки матриц на равенство
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для выполнения проверки на равенство размеры матриц должны совпадать!")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return self.matrix == other.matrix

    def __gt__(self, other):
        """
        Метод проверки матриц на знак >
        """
        sub_matrix = Matrix.__sub__(self, other)
        for i in range(len(sub_matrix.matrix)):
            for j in range(len(sub_matrix.matrix[0])):
                if sub_matrix.matrix[i][j] < 0:
                    return False
        return self.matrix > other.matrix


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 0]])
    matrix_5 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])
    print(f'\nmatrix_1\n{matrix_1}')
    print(f'\nmatrix_2\n{matrix_2}')
    print(f'\nmatrix_5\n{matrix_5}')
    add_matrix_1_2 = matrix_1 + matrix_2
    print(f'\nmatrix_1 + matrix_2 =>\n{add_matrix_1_2}')
    print(f'\nПроверка matrix_1 == matrix_2 => {matrix_1 == matrix_2}')
    print(f'\nПроверка matrix_1 == matrix_5 => {matrix_1 == matrix_5}')
    matrix_3 = Matrix([[1, 2], [3, 4]])
    matrix_4 = Matrix([[5, 6], [7, 8]])
    print(f'\nMatrix_3\n{matrix_3}')
    print(f'\nMatrix_4\n{matrix_4}')
    mul_matrix_3_4 = matrix_3 * matrix_4
    print(f'\nmatrix_3 * matrix_4 =>\n{mul_matrix_3_4}')
    sub_matrix_4_3 = matrix_4 - matrix_3
    print(f'\nmatrix_4 - matrix_3 =>\n{sub_matrix_4_3}')
    print(f'\nmatrix_4 > matrix_3 => {matrix_4 > matrix_3}')
