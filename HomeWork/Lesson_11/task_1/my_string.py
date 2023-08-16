import time

__all__ = ['MyString']


class MyString(str):
    """
    If you use string, this class will also show you creator's name time creating an object
    """
    def __new__(cls, text: str, creator: str):
        """
        Gives extra information about your string
        :param text: entry string
        :param creator: name's creator
        """
        print('__new__ started')
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        Print not only text, but also name's creator and time creating
        """
        return f'{super().__str__()} created by: {self.creator} at {self.time}'


if __name__ == '__main__':
    example = MyString('text', 'Lisa')
    example_2 = MyString('text2', 'Oly')
    print(example)
    print(example_2)
    print(help(MyString))
    print(MyString.__doc__)
    print(MyString.__new__.__doc__)
