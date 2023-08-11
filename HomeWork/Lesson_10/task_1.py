# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Animal:
    def __init__(self, name: str, color: str, size: str):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass

    def speak(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: str, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(self.max_depth)

    def speak(self):
        print('буль-буль')


class Bird(Animal):
    def __init__(self, name: str, color: str, size: str, habitat: str):
        super().__init__(name, color, size)
        self.habitat = habitat

    def show_unique(self):
        print(self.habitat)

    def speak(self):
        print('чик-чирик')


class Cat(Animal):
    def __init__(self, name: str, color: str, size: str, hairy: bool):
        super().__init__(name, color, size)
        self.hairy = hairy

    def show_unique(self):
        print(self.hairy)

    def speak(self):
        print('мяу-мяу')


class AnimalFactory:
    def __new__(cls, type_class, *args):
        instance = type_class(*args)
        return instance


if __name__ == '__main__':
    fish = AnimalFactory(Fish, 'Fly', 'orange', 10.2, 15.0)
    bird = AnimalFactory(Bird, 'Chichi', 'white', 82.3, 'Forest')
    cat = AnimalFactory(Cat, 'Tom', 'black', 11, True)

    animals = (fish, bird, cat)
    for a in animals:
        a.show_unique()
        a.speak()
