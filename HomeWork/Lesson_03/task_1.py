# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

some_list = [2, 3, 2, 4, 3, 2, 1, 2, 2, 7, 5, 4, 8, 6, 3, 5]
duplicates = []
i = 0

while i < len(some_list):
    if some_list.count(some_list[i]) > 1:
        for _ in range(1, (some_list.count(some_list[i]))):
            duplicates.append(some_list.pop(some_list.index(some_list[i], i + 1)))
    i += 1

print(f"Дубликаты:             {duplicates}\nРезультирующий список: {some_list}")

