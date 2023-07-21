# ✔ Напишите функцию для транспонирования матрицы


def transpose(num_matrix):
    """Функция для транспонирования матрицы"""
    res = []
    row = len(num_matrix)
    colum = len(num_matrix[0])
    for j in range(colum):
        tmp = []
        for i in range(row):
            tmp = tmp + [num_matrix[i][j]]
        res = res + [tmp]
    return res


matrix = [[1, 2, 4, 5],
          [6, 7, 8, 9],
          [0, 11, 12, 13]]
print("ИСХОДНАЯ МАТРИЦА: \n\t" + '\n\t'.join(list(map(str, matrix))))
print("ТРАНСПОНИРОВАНИЕ МАТРИЦЫ С ПОМОЩЬЮ ФУНКЦИИ: \n\t" + '\n\t'.join(list(map(str, transpose(matrix)))))
# решение с использованием zip() (zip() возвращает элементы в кортеже -> в списке!)
print("ТРАНСПОНИРОВАНИЕ МАТРИЦЫ С ПОМОЩЬЮ ФУНКЦИИ zip():\n\t" +
      '\n\t'.join(list(map(str, [list(line) for line in zip(*matrix)]))))
