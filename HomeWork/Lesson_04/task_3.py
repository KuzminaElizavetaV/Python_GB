# ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


def print_menu(cash_print):
    """Функция для печати меню банкомата"""
    print(f"На вашем счете = {round(cash_print, 2)} рублей\n\tМЕНЮ:\n1 -> пополнить\n2 -> снять\n"
          f"3 -> история операций\n4 -> выход")
    return cash_print


def put_money(cash_1_op, count_1_op):
    """Функция для внесения денег"""
    add = float(input("внесите сумму кратную 50: "))
    if add % 50 == 0:
        cash_1_op += add
        count_1_op += 1
        op_history.append(f"пополнение счета на {str(add)} рублей, баланс: {round(cash_1_op, 2)} рублей")
        return cash_1_op, count_1_op
    else:
        print("Ошибка: внесена некорректная сумма!")
        op_history.append("Ошибка: внесена некорректная сумма!")
        count_1_op += 1
        return cash_1_op, count_1_op


def give_money(cash_2_op, count_2_op):
    """Функция для снятия денег"""
    take = float(input("введите сумму снятия кратную 50: "))
    if take % 50 == 0:
        percent = take * 1.5 * 0.01
        if percent < 30:
            percent = 30
        if percent > 600:
            percent = 600

        if cash_2_op < (take + percent):
            print("Ошибка: на вашем счету недостаточно денежных средств!")
            op_history.append("Ошибка: на вашем счету недостаточно денежных средств!")
            count_2_op += 1
            return cash_2_op, count_2_op
        else:
            cash_2_op -= (take + percent)
            count_2_op += 1
            op_history.append(f"Снятие {str(take)} рублей, баланс: {round(cash_2_op, 2)} рублей")
            return cash_2_op, count_2_op
    else:
        print("Ошибка: некорректная сумма!")
        op_history.append("Ошибка: некорректная сумма!")
        count_2_op += 1
        return cash_2_op, count_2_op


def print_history(print_op_history):
    """Функция для печати истории операций"""
    print("\nистория операций: " + "\n".join(print_op_history) + "\nдля продолжения нажмите любую клавишу...")


def give_percent(cash_3_op, count_3_op):
    """Функция начисления процентов за каждую третью операцию в банкомате"""
    if count_3_op % 3 == 0:
        cash_3_op *= 1.03
        print(f"-> Операция № {count_3_op}! Каждая 3-я операция, банк начислил проценты, баланс счета = {cash_3_op}")
    return cash_3_op


def cash_machine(total_cash, count, history_operation):
    """функция банкомата ! cash_machine !"""
    while True:
        if total_cash > 5_000_000:
            total_cash *= 0.9

        total_cash = print_menu(total_cash)

        action = input("\nваш выбор -> ")
        match action:
            case "1":
                total_cash, count = put_money(total_cash, count)
            case "2":
                total_cash, count = give_money(total_cash, count)
            case "3":
                print_history(history_operation)
                count += 1
            case "4":
                quit()
        total_cash = give_percent(total_cash, count)


# ----------------входные данные и запуск банкомата-----------------------
cash = 0
operation_counter = 0
op_history = []
cash_machine(cash, operation_counter, op_history)
