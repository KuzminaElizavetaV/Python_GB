# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX_DIVIDER = 16
HEX_STRING = "0123456789abcdef"


def get_number_from_user() -> int:
    r = input("Введите число: ")
    return int(r)


def converter(patient: int) -> str:
    r: str = ""
    while patient > 0:
        r = str(HEX_STRING[patient % HEX_DIVIDER]) + r
        patient //= HEX_DIVIDER
    return "РЕЗУЛЬТАТ: " + r


pat = get_number_from_user()
if isinstance(pat, int):
    print(converter(pat))
else:
    print("Неверно. Попробуйте снова")

print("ПРОВЕРКА: ", hex(pat)[2:])
