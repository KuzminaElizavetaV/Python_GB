# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def file_path(absolute_path: str) -> tuple:
    """Функция, которая принимает на вход строку — абсолютный путь до файла.
    Возвращает кортеж из трёх элементов: путь, имя файла, расширение файла"""
    absolute_path = absolute_path.replace(".", " ").replace("\\", " ")
    *path, file_name, extension = absolute_path.split()
    res = "\\".join(path), file_name, extension
    return res


path_1 = "D:\Python_GB\HomeWork\Lesson_05\\task_1.py"
print(file_path(path_1))
