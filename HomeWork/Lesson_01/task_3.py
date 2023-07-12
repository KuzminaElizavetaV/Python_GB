# ✔ Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1001)
attempts = 0
print("***УГАДАЙ ЧИСЛО ЗА 10 попыток***")

while attempts < 10:
    input_num = int(input("Введите число от 0 до 1000: "))
    if input_num == num:
        print("Вы угадали!")
        break
    elif input_num > num:
        print("Это число больше загаданного числа")
    else:
        print("Это число меньше загаданного числа")
    attempts += 1
print("Программа загадала вот такое число -> ", num)
