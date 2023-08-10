# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from os.path import exists
from random import randint
from typing import Callable

FILE_NAME_CSV = 'numbers.csv'


def generate_nums2csv():
    """
    Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк
    """
    quant = randint(100, 1000)
    with open(FILE_NAME_CSV, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for _ in range(quant):
            writer.writerow([randint(-50, 50) for _ in range(3)])


def save_log2json(func: Callable):
    """
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
    :param func: функция
    """
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        data = []
        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_read:
                data = json.load(json_read)
        result = func(*args, **kwargs)
        cur_data = {'args': args,
                    'roots': func(*args, **kwargs)
        }
        data.append(cur_data)
        with open(file_path, 'w', encoding='utf-8') as json_write:
            json.dump(data, json_write, indent=2, ensure_ascii=False)
        return result
    return wrapper


def find_roots_from_csv(func: Callable):
    """
    Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    :param func: функция
    """
    def wrapper(*args, **kwargs):
        with open(FILE_NAME_CSV, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                a, b, c = map(int, line)
                func(a, b, c)
        result = func(*args, **kwargs)
        return result

    return wrapper


@find_roots_from_csv
@save_log2json
def find_roots(a: int, b: int, c: int):
    """
    Функция нахождения корней квадратного уравнения
    :param a: коэффициент а тип int
    :param b: коэффициент b тип int
    :param c: коэффициент c тип int
    """
    discr = b ** 2 - 4 * a * c
    if discr > 0 and a != 0:
        x1 = (-b + discr ** (1 / 2)) / (2 * a)
        x2 = (-b - discr ** (1 / 2)) / (2 * a)
        return f'X1 = {x1}, X2 = {x2}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'X = {x}'
    else:
        return 'корней нет'


if __name__ == '__main__':
    generate_nums2csv()
    find_roots(1, 2, -3)
