# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

class CashMachine:
    __FREE_LIMIT = 5_000_000
    __COMMISSION_BANK = 0.9
    __DIVISION_CHECK = 50
    __MIN_COMMISSION = 30
    __COMMISSION = 1.5
    __MAX_COMMISSION = 600
    __BONUS_OPERATION = 3
    __BONUS_PERCENT = 1.03

    def __init__(self, balance: int = 0, counter: int = 0, history: list = None):
        """
        Метод инициализации экземпляра класса банкомата (CashMachine)
        :param balance: баланс
        :param counter: счетчик операций
        :param history: история операций
        """
        self.__cash = balance
        self.__counter = counter
        if history is None:
            self.__history = []
        else:
            self.__history = history

    def __print_menu(self):
        """Метод печати меню банкомата"""
        print(f'      МЕНЮ:\nБАЛАНС СЧЕТА = {round(self.__cash, 2)}\n'
              f'1. ПОПОЛНИТЬ\n2. СНЯТЬ\n3. ИСТОРИЯ ОПЕРАЦИЙ\n4. ВЫЙТИ')

    def __put_money(self):
        """Метод внесения денег"""
        add = float(input("Внесите сумму, кратную 50: "))
        if add % self.__DIVISION_CHECK == 0:
            self.__cash += add
            self.__history.append(f"пополнение счета на {str(add)} рублей, баланс: {round(self.__cash, 2)} рублей")
        else:
            print("Ошибка! Внесена некорректная сумма!")
            self.__history.append(f"Ошибка! Внесена некорректная сумма!, баланс: {round(self.__cash, 2)} рублей")

    def __give_money(self):
        """Метод снятия денег"""
        take = float(input("Введите сумму, кратную 50: "))
        if take % self.__DIVISION_CHECK == 0:
            percent = take * 0.01 * self.__COMMISSION
            if percent < self.__MIN_COMMISSION:
                percent = self.__MIN_COMMISSION
            if percent > self.__MAX_COMMISSION:
                percent = self.__MAX_COMMISSION
            if self.__cash < (take + percent):
                print(f"Ошибка! На счету недостаточно денежных средств, баланс: {round(self.__cash, 2)} рублей")
                self.__history.append(f"Ошибка! На счету недостаточно денежных средств, "
                                      f"баланс: {round(self.__cash, 2)} рублей")
            else:
                self.__cash -= (take + percent)
                self.__history.append(f"Снятие {str(take)} рублей, "
                                      f"баланс: {round(self.__cash, 2)} рублей (комиссия банка {percent} рублей)")
        else:
            print("Ошибка! Неверная сумма!")
            self.__history.append(f"Ошибка! Неверная сумма, баланс: {round(self.__cash, 2)} рублей")

    def __print_history(self):
        """Метод печати истории операций"""
        print("\nИстория операций: ")
        print(" \n".join(self.__history))
        input("для продолжения нажмите клавишу ENTER...")

    def __give_percent(self):
        """Метод начисления процентов за каждую третью операцию в банкомате"""
        if self.__counter % self.__BONUS_OPERATION == 0:
            self.__cash *= self.__BONUS_PERCENT
            print(f"-> {self.__counter} операция! Банк начислил проценты по вкладу!")
            self.__history.append(f"-> {self.__counter} операция!"
                                  f" Банк начислил проценты по вкладу! Баланс: {round(self.__cash, 2)} рублей")

    def work(self):
        """Метод работы банкомата"""
        while True:
            self.__counter += 1
            if self.__cash > self.__FREE_LIMIT:
                self.__cash *= self.__COMMISSION_BANK
                print(f'Комиссия банка 10%, баланс: {round(self.__cash, 2)} рублей')
                self.__history.append(f'Комиссия банка 10%, баланс: {round(self.__cash, 2)} рублей')

            self.__print_menu()

            action = input("\nВаш выбор -> ")
            match action:
                case "1":
                    self.__put_money()
                case "2":
                    self.__give_money()
                case "3":
                    self.__print_history()
                case "4":
                    quit()
            self.__give_percent()


if __name__ == "__main__":
    cash_machine = CashMachine()
    cash_machine.work()
