def check_queens(pos) -> bool:
    """Определяет, есть ли среди ферзей пара бьющих друг друга."""
    beats = True
    for i in range(len(pos)):
        row, col = pos[i]
        for j in range(i + 1, len(pos)):
            row_2, col_2 = pos[j]
            if row == row_2 or col == col_2 or abs(row - row_2) == abs(col - col_2):
                beats = False
    return beats


def print_check_result(pos):
    if check_queens(pos):
        print("Ферзи не бьют друг друга")
    else:
        print("Ферзи бьют друг друга")


if __name__ == "__main__":
    print("Это модуль !")
