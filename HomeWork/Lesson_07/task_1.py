# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри
# каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os


def create_sequence_number(num: int):
    """
    Функция-генератор создания порядкового номера
    :param num: количество цифр в порядковом номере
    """
    limit = 9999999
    countdown = 1 if num == 1 else (10 ** num) + 1
    for i in range(countdown, limit):
        yield i


def rename_files(number_of_digits: int, original_extension: str, end_extension: str, original_range: list[1, 0],
                 end_filename: str = ""):
    """
    Функция группового переименования файлов
    :param number_of_digits: количество цифр в порядковом номере
    :param original_extension: расширение исходного файла (без точки)
    :param end_extension: расширение конечного файла (без точки)
    :param original_range: диапазон сохраняемого оригинального имени (по умолчанию не берет старое имя)
    :param end_filename: конечное имя файлов (по умолчанию не добавляет)
    """
    serial_number = create_sequence_number(number_of_digits)
    print(type(original_range))
    start, end = original_range
    for file in os.listdir():
        if ("." + original_extension) in file:
            if number_of_digits > 1:
                new_filename = f'{file.split(".")[0][start - 1:end]}_{end_filename}_' \
                           f'{str(next(serial_number))[1:]}.{end_extension}'
            else:
                new_filename = f'{file.split(".")[0][start - 1:end]}-{end_filename}_' \
                           f'{str(next(serial_number))}.{end_extension}'
            os.rename(file, new_filename)


if __name__ == '__main__':
    rename_files(4, "txt", "txt", [2, 5], end_filename="rename")
