from os import path, listdir, walk
import csv
import json
import pickle
__all__ = ['make_json', 'data2json', 'json2csv', 'change_csv2json', 'json2pickle', 'list_of_dicts_pickle2csv',
           'csv2pickle_string', 'all_info_dir']

FILE_NAME_JSON_1 = r"D:\Python_GB\HomeWork\Lesson_08\task_2\result.json"
FILE_NAME_TXT = r"D:\Python_GB\HomeWork\Lesson_07\result.txt"
FILE_NAME_JSON_2 = r"D:\Python_GB\HomeWork\Lesson_08\task_2\json_data.json"
FILE_NAME_CSV_1 = r"D:\Python_GB\HomeWork\Lesson_08\task_2\json_data.csv"
FILE_NAME_JSON_3 = r"D:\Python_GB\HomeWork\Lesson_08\task_2\csv_data.json"
DIR_PATH = r"D:\Python_GB\HomeWork\Lesson_08\task_2"
FILE_NAME_PICKLE = r"D:\Python_GB\HomeWork\Lesson_08\task_2\csv_data.pickle"
FILE_NAME_CSV = r"D:\Python_GB\HomeWork\Lesson_08\task_2\csv_data_pickle.csv"
DIR_PATH_ = r'D:\Python_GB\HomeWork\Lesson_08'
FILE_NAME_START = 'ALL_INFO_DIR_'
TYPE_OBJECT = ('файл', 'директория')
OBJECT_INFO_KEYS = ('ОБЪЕКТ_НОМЕР_', 'РОДИТЕЛЬСКАЯ_ДИРЕКТОРИЯ', 'ТИП_ОБЪЕКТА', 'ИМЯ_ОБЪЕКТА', 'РАЗМЕР_В_БАЙТАХ')


def make_json(path_txt_file: str = FILE_NAME_TXT, path_json_file: str = FILE_NAME_JSON_1) -> None:
    """
    Функция создает файл в формате JSON из текстового файла, где каждая строка вида str|int или float,
    например, АЛЗХНРМ|81867 или алзхнрм|545352.75
    :param path_txt_file: путь к файлу.txt
    :param path_json_file: путь к файлу.json
    """
    nums_names_dict = {}
    with open(path_txt_file, 'r', encoding='utf-8') as file_txt:
        for line in file_txt:
            name, num = line.split('|')
            nums_names_dict[name.capitalize()] = float(num)
    with open(path_json_file, 'w', encoding='utf-8') as file_json:
        json.dump(nums_names_dict, file_json, ensure_ascii=False, indent=2)


def data2json(json_file_path: str = FILE_NAME_JSON_2) -> None:
    """
    Функция в цикле запрашивает от пользователя: имя, личный идентификатор, уровень доступа (от 1 до 7)
    и добавляет эту информацию в файл.json, где данные группируются по уровню доступа, а идентификатор пользователя
    выступает ключём для имени
    :param json_file_path: путь к файлу.json
    """
    users_id = set()
    if path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            for user in data.values():
                users_id.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}
    while True:
        name = input('Введите имя: ')
        if not name:
            break
        _id = input('Введите ID: ')
        access_level = input('Введите уровень доступа: ')
        if _id in users_id:
            continue
        data[access_level][_id] = name
        with open(json_file_path, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, ensure_ascii=False, indent=2)


def json2csv(json_file_path: str = FILE_NAME_JSON_2, csv_file_path: str = FILE_NAME_CSV_1) -> None:
    """
    Функция сохраняет файл.json, созданный функцией data2json, в файл.csv
    :param json_file_path: путь к файлу.json
    :param csv_file_path: путь к файлу.scv
    :return:
    """
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    rows = []
    for access_level, users in data.items():
        for user_id, name in users.items():
            rows.append({'access_level': int(access_level), 'id': int(user_id), 'name': name})
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=['access_level', 'id', 'name'])
        csv_dict.writeheader()
        csv_dict.writerows(rows)


def change_csv2json(csv_file_path: str = FILE_NAME_CSV_1, json_file_path: str = FILE_NAME_JSON_3) -> None:
    """
    Функция открывает на чтение файл.csv, созданный функцией json2csv без изспользования csv.DictReader,
    дополняет id до 10 цифр незначащими нулями, делает первую букву имени прописной, добавляет поле хэш
    на основе имени и идентификатора, сохраняет записи файл.json, где каждая строка файла.csv представлена
    как отдельный json словарь
    :param csv_file_path: путь к файлу.scv
    :param json_file_path: путь к файлу.json
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel-tab')
        data = []
        for i, row in enumerate(csv_reader):
            if i:
                access_level, user_id, name = row
                data.append({'access_level': int(access_level),
                             'user_id': f'{int(user_id):010}',
                             'name': name.capitalize(),
                             'hash': hash((user_id, name))})
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)


def json2pickle(dir_path: str = DIR_PATH) -> None:
    """
    Функция ищет файлы.json в директории и сохраняет их содержимое в виде одноимённых файлов.pickle
    :param dir_path: путь к директории
    """
    json_files = filter(lambda file_name: file_name[-5:] == '.json', listdir(dir_path))
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            data = json.load(json_reader)
        with open(f'{json_file[:-5]}.pickle', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)


def list_of_dicts_pickle2csv(pickle_file_path: str = FILE_NAME_PICKLE, csv_file_path: str = FILE_NAME_CSV) -> None:
    """
    Функция преобразует файл.pickle, хранящий список словарей, в табличный файл.csv, извлекая ключи словаря из
    файла.pickle для заголовков столбца
    :param pickle_file_path: путь к файлу.pickle
    :param csv_file_path: путь к файлу.csv
    """
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    headers = data[0].keys()
    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def csv2pickle_string(csv_file_path: str = FILE_NAME_CSV) -> None:
    """
    Функция читает файл.csv, созданный функцией pickle_list_of_dicts2csv, без использования csv.DictReader и
    распечатывает его как pickle строку
    :param csv_file_path: путь к файлу.csv
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')
        data_list = []
        headers = []
        for i, row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key: value for key, value in zip(headers, row)}
                data_list.append(row_data)
    print(pickle.dumps(data_list))


def get_size(path_object: str) -> int:
    """
    Функция подсчета суммарного размера файлов директории в байтах с учётом всех вложенных файлов и директорий
    :param path_object: путь к директории
    :return: int = размер директории
    """
    total: int = 0
    for path_dir, dirs, files in walk(path_object):
        for file in files:
            path_file = path.join(path_dir, file)
            total += path.getsize(path_file)
    return total


def all_info_dir(dir_path: str = DIR_PATH) -> None:
    """
        Функция рекурсивно обходит директорию и все ее вложенные директории. Результаты сохраняются в файлы форматов:
        json, csv, pickle.
        ○ для дочерних объектов указана родительская директория.
        ○ для каждого объекта указано файл это или директория.
        ○ для файлов сохраняется его размер в байтах, а для директорий суммарный размер файлов в ней с учётом всех
        вложенных файлов и директорий.
        :param dir_path: путь к директории
        """
    list_objects = []
    dict_objects = {}
    list_objects_2 = []
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
            dict_objects[f'{OBJECT_INFO_KEYS[0].capitalize()}{i}'] = dict(object_info)
    for object_num, _object_info in dict_objects.items():
        list_objects_2.append({OBJECT_INFO_KEYS[0]: object_num,
                               OBJECT_INFO_KEYS[1]: _object_info[OBJECT_INFO_KEYS[1]],
                               OBJECT_INFO_KEYS[2]: _object_info[OBJECT_INFO_KEYS[2]],
                               OBJECT_INFO_KEYS[3]: _object_info[OBJECT_INFO_KEYS[3]],
                               OBJECT_INFO_KEYS[4]: _object_info[OBJECT_INFO_KEYS[4]]})
    dir_name = dir_path.split('\\')[-1]
    with open(f'{FILE_NAME_START}{dir_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict_objects, json_file, indent=2, ensure_ascii=False)
    with open(f'{FILE_NAME_START}{dir_name}_v1.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=list_objects_2[0].keys())
        writer.writeheader()
        writer.writerows(list_objects_2)
    with open(f'{FILE_NAME_START}{dir_name}_v2.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, dialect='excel-tab', fieldnames=list_objects[0].keys())
        writer.writeheader()
        writer.writerows(list_objects)
    with open(f'{FILE_NAME_START}{dir_name}.pickle', 'wb') as pickle_file:
        pickle.dump(dict_objects, pickle_file)
