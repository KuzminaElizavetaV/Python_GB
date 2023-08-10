from os import walk, path
import json
import csv
import pickle
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
#   файлов и директорий.
DIR_PATH = r'D:\Python_GB\HomeWork\Lesson_07'
FILE_NAME_START = 'ALL_INFO_DIR_'
TYPE_OBJECT = ('файл', 'директория')
OBJECT_INFO_KEYS = ('ОБЪЕКТ_НОМЕР_', 'РОДИТЕЛЬСКАЯ_ДИРЕКТОРИЯ', 'ТИП_ОБЪЕКТА', 'ИМЯ_ОБЪЕКТА', 'РАЗМЕР_В_БАЙТАХ')


def get_size(path_object: str) -> int:
    total: int = 0
    for path_dir, dirs, files in walk(path_object):
        for file in files:
            path_file = path.join(path_dir, file)
            total += path.getsize(path_file)
    return total


def all_info_dir(dir_path: str = DIR_PATH) -> None:
    list_objects = []
    dict_objects = {}
    for root, dirs, files in walk(dir_path):
        for name in files:
            full_path = path.join(root, name)
            list_objects.append({OBJECT_INFO_KEYS[1]: root,
                                 OBJECT_INFO_KEYS[2]: TYPE_OBJECT[0],
                                 OBJECT_INFO_KEYS[3]: name,
                                 OBJECT_INFO_KEYS[4]: path.getsize(full_path)})
        for name in dirs:
            full_path = path.join(root, name)
            list_objects.append({OBJECT_INFO_KEYS[1]: root,
                                 OBJECT_INFO_KEYS[2]: TYPE_OBJECT[1],
                                 OBJECT_INFO_KEYS[3]: name,
                                 OBJECT_INFO_KEYS[4]: get_size(full_path)})
        for i, object_info in enumerate(list_objects, start=1):
            dict_objects[f'{OBJECT_INFO_KEYS[0]}{i}'] = dict(object_info)
    dir_name = dir_path.split('\\')[-1]
    with open(f'{FILE_NAME_START}{dir_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict_objects, json_file, indent=2, ensure_ascii=False)
    with open(f'{FILE_NAME_START}{dir_name}_v1.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=[OBJECT_INFO_KEYS[0], OBJECT_INFO_KEYS[1],
                                                                           OBJECT_INFO_KEYS[2], OBJECT_INFO_KEYS[3],
                                                                           OBJECT_INFO_KEYS[4]])
        writer.writeheader()
        rows = []
        for object_num, _object_info in dict_objects.items():
            rows.append({OBJECT_INFO_KEYS[0]: str(object_num), OBJECT_INFO_KEYS[1]: _object_info[OBJECT_INFO_KEYS[1]],
                         OBJECT_INFO_KEYS[2]: _object_info[OBJECT_INFO_KEYS[2]],
                         OBJECT_INFO_KEYS[3]: _object_info[OBJECT_INFO_KEYS[3]],
                         OBJECT_INFO_KEYS[4]: _object_info[OBJECT_INFO_KEYS[4]]})
        writer.writerows(rows)
    with open(f'{FILE_NAME_START}{dir_name}_v2.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=list_objects[0].keys())
        writer.writeheader()
        writer.writerows(list_objects)
    with open(f'{FILE_NAME_START}{dir_name}.pickle', 'wb') as pickle_file:
        pickle.dump(dict_objects, pickle_file)


all_info_dir()
