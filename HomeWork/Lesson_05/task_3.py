# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fib(n):
    """Функция вычисления числа Фибоначчи"""
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_generator(n):
    """Функция генератор чисел Фибоначчи"""
    for i in range(1, n + 1):
        yield f"{i:>2}  число Фибоначчи = {fib(i):>2}"


# 2 вариант с циклом
def fib_for(arg):
    """Функция генератор чисел Фибоначчи"""
    fib1 = 1
    fib2 = 1
    for i in range(arg):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib_sum


num = 10
iter_fib_generator = iter(fib_generator(num))
for _ in range(num):
    print(next(iter_fib_generator))
print("2 вариант")
iter_fib_for = iter(fib_for(num))
for _ in range(num):
    print(next(iter_fib_for))
