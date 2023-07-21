# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def function_accept_key_param(**kwargs) -> dict:
    """Функция принимает на вход только ключевые параметры и возвращает словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента"""
    dict_res = {}
    for key, value in kwargs.items():
        if isinstance(value, dict | list | set):
            dict_res[str(value)] = key
        else:
            dict_res[value] = key
    return dict_res


res = function_accept_key_param(one=False, two={2, "Dima"}, three=3, my_set={1, 2, 3, 4}, five=[10, 20, 30])
print(res)
