__all__ = ['Archive']


class Archive:
    """
    Хранит пару свойств строк и чисел.
    """
    _instance = None

    def __init__(self, text: str, num: int):
        print('__init__')
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        Добавляет строки и номера в списки
        """
        print('__new__')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_text = []
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_text.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        """
        Вывод объекта Архив в виде строки
        """
        return f'We have text: {self.text} and number: {self.num}\nArchive texts: {self.archive_text}\n' \
               f'Archive nums: {self.archive_nums}'

    def __repr__(self):
        return f'We have text: {self.text} and number: {self.num}'


if __name__ == '__main__':
    inst_1 = Archive('text', 12)
    inst_2 = Archive('text-2', 10)
    inst_3 = Archive('text-3', 7)
    print(Archive.__new__.__doc__)
    print(inst_1)
    print(inst_3)
    print(inst_2)
