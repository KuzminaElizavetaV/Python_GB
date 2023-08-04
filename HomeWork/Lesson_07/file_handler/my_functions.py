from random import randint, uniform, sample, shuffle, choices
from string import ascii_lowercase, digits
import typing as text_io
from os import path, chdir, mkdir, listdir, replace, getcwd, rename
__all__ = ["write_rnd_nums_file", "generic_names", "create_file_from_two_files", "make_files", "make_difference_files",
           "make_files_to_dir", "sort_files_move_directories", "rename_files"]

MAX_INT = 1000
MIN_INT = -1000
VOWEL = 'аеиоуэюя'
CONSONANT = 'бвгджзклмнопрстфхцшщ'
FILE_GEN_NAMES = 'names.txt'
FILE_RND_NUMS = 'numbers.txt'
FILE_RESULT = 'result.txt'
MIN_LEN_NAME = 4
MAX_LEN_NAME = 7
FILE_TYPE_DICT = {'Video': ['avi', 'mov', 'mp4'],
                  'Pictures': ['bmp', 'jpg', 'png', 'jpeg', 'gif'],
                  'Text': ['txt', 'doc', 'docx'],
                  'Music': ['mp3', 'wav', 'wma', 'aac']
                  }
LIMIT_SEQ_NUM = 999999


def write_rnd_nums_file(amount_string: int, filename: str = FILE_RND_NUMS):
    """
    Функция заполнения файла случайными парами чисел добавлением в конец в диапазоне от -1000 до 1000.
    Первое число int, второе - float, разделенные вертикальной чертой.
    :param amount_string: количество строк
    :param filename: имя файла (по умолчанию принимает значение константы FILE_RND_NUMS)
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(amount_string):
            file.write(f'{randint(MIN_INT, MAX_INT)}|{round(uniform(MIN_INT, MAX_INT), 2)}\n')


def generic_names():
    """
    Функция генерации одного псевдоимени из гласных и согласных звуков кириллицы длиной от 4 до 7 букв
    """
    len_name = randint(MIN_LEN_NAME, MAX_LEN_NAME)
    num_vowels = randint(1, len_name - 2)
    name = sample(VOWEL, num_vowels) + sample(CONSONANT, len_name - num_vowels)
    shuffle(name)
    with open(FILE_GEN_NAMES, 'a', encoding='utf-8') as f:
        f.write(''.join(name).title() + '\n')


def readline_or_begin(file: text_io) -> str:
    """
    Функция чтения строк из файла. При достижении конца файла, возвращает каренку в его начало.
    :param file: имя файла
    :return: строка из файла
    """
    text = file.readline()
    if text == '':
        # перенос каретки вначало файла
        file.seek(0)
        text = file.readline()
    return text[:-1]


def create_file_from_two_files():
    """
    Функция открывает на чтение созданные файлы с числами и псевдоименами, Перемножает пары чисел.
    В новый файл сохраняет псевдоимя и произведение:
        ✔ если результат умножения отрицательный, сохраняет имя строчными буквами и произведение по модулю
        ✔ если результат умножения положительный, сохраняет имя прописными буквами и произведение округлённое до целого.
    В результирующем файле столько же строк, сколько в более длинном файле.
    При достижении конца короткого файла, возвращает каренку в его начало.
    """
    with (
        open(FILE_RND_NUMS, 'r', encoding='utf-8') as numbers,
        open(FILE_GEN_NAMES, 'r', encoding='utf-8') as names,
        open(FILE_RESULT, 'w', encoding='utf-8') as res
    ):
        len_numbers = len(numbers.readlines())
        len_names = len(names.readlines())
        for _ in range(max(len_numbers, len_names)):
            cur_name = readline_or_begin(names)
            cur_number = readline_or_begin(numbers)
            cur_number1, cur_number2 = cur_number.split('|')
            prod = int(cur_number1) * float(cur_number2)
            if prod > 0:
                res.write(f'{cur_name.upper()}|{str(round(prod))}\n')
            else:
                res.write(f'{cur_name.lower()}|{str(-prod)}\n')


def make_files(ext: str, max_name_len: int = 30, min_name_len: int = 6, min_byte: int = 256, max_byte: int = 4096,
               quantity: int = 42) -> None:
    """
    Функция создаёт файлы с указанным расширением. Имя файла и размер находятся в рамках переданного диапазона.
    :param ext: расширение файла
    :param max_name_len: максимальная длина случайно сгенерированного имени, по умолчанию 30
    :param min_name_len: минимальная длина случайно сгенерированного имени, по умолчанию 6
    :param min_byte: минимальное число случайных байт, записанных в файл, по умолчанию 256
    :param max_byte: максимальное число случайных байт, записанных в файл, по умолчанию 4096
    :param quantity: количество файлов, по умолчанию 42
    """
    for i in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        byte_array = bytes(randint(0, 255) for _ in range(randint(min_byte, max_byte)))
        with open(rf'{name}.{ext}', 'wb') as files:
            files.write(byte_array)


def make_difference_files(**kwargs):
    """
    Функция создания файлов с разными расширениями.
    :param kwargs: расширения и количество файлов, например (txt=3, jpg=5, bmp=6, doc=7)
    """
    for ext, quantity in kwargs.items():
        make_files(ext=ext, quantity=quantity)


def make_files_to_dir(directory: str, **kwargs) -> None:
    """
    Функция создания файлов в указанную директорию
    :param directory: название директории
    :param kwargs: расширения и количество файлов, например (txt=3, jpg=5, bmp=6, doc=7)
    :return:
    """
    if not path.exists('.\\' + directory):
        mkdir(directory)
    chdir(directory)
    make_difference_files(**kwargs)


def sort_files_move_directories():
    """
    Функцию сортировки файлов по директориям: видео, изображения, текст и т.п.
    ✔ Каждая группа включает файлы с несколькими расширениями.
    ✔ В исходной директории остатются файлы, которые не подошли для сортировки.
    """
    for file in listdir():
        extension = file.split('.')[-1]
        for key, value in FILE_TYPE_DICT.items():
            if extension in value:
                directory = key
                if not path.exists(directory):
                    mkdir(directory)
                replace(file, path.join(getcwd(), directory, file))


def create_sequence_number(num: int):
    """
    Функция-генератор создания порядкового номера
    :param num: количество цифр в порядковом номере
    """
    countdown = 1 if num == 1 else (10 ** num) + 1
    for i in range(countdown, LIMIT_SEQ_NUM):
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
    for file in listdir():
        if ("." + original_extension) in file:
            if number_of_digits > 1:
                new_filename = f'{file.split(".")[0][start - 1:end]}_{end_filename}_' \
                           f'{str(next(serial_number))[1:]}.{end_extension}'
            else:
                new_filename = f'{file.split(".")[0][start - 1:end]}-{end_filename}_' \
                           f'{str(next(serial_number))}.{end_extension}'
            rename(file, new_filename)
