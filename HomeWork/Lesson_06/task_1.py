# 📌 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты напроверку.
from sys import argv
__all__ = ["check_date"]


def is_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    day, mon, year = map(int, str_date.split("."))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        return False
    if mon in (4, 6, 9, 11) and day > 30:
        return False
    if mon == 2 and is_leap(year) and day > 29:
        return False
    if mon == 2 and not is_leap(year) and day > 28:
        return False
    return True


if __name__ == "__main__":
    print(check_date(*(argv[1:])))
