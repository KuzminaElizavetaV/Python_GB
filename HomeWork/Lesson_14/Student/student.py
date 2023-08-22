import csv
from os import path
from HomeWork.Lesson_14.Student.student_exceptions import StudentNameError, NameSubjectError, StudentGradeError, \
    StudentTestResultError
FILE_NAME_CSV = "D:\\Python_GB\\HomeWork\\Lesson_14\\Student\\student_subjects.csv"
HEADER_GRADE_BOOK = 'ЖУРНАЛ УСПЕВАЕМОСТИ СТУДЕНТА'
MIN_TEST_SCORE = 0
MAX_TEST_SCORE = 100
MIN_GRADE = 2
MAX_GRADE = 5
__all__ = ['Student']


class CheckName:
    """
    Дескриптор класса Student для проверки имени
    """
    def __set_name__(self, owner, name_str):
        self.name_str = '__' + name_str

    def __get__(self, instance, owner):
        return getattr(instance, self.name_str)

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise StudentNameError(value)
        else:
            setattr(instance, self.name_str, value)


class Student:
    """
    Класс реализует модель студент-успеваемость.
    При создании экземпляра класса ему создается журнал успеваемости. Названия предметов загружаются из файла
    student_subject.csv, по каждому предмету можно ставить оценки от 2 до 5 баллов включительно и вносить результаты
    за тестирование от 0 до 100 баллов включительно. Структура хранения данных - словарь.
    """
    surname = CheckName()
    name = CheckName()
    name_father = CheckName()
    __grades = 'Оценки'
    __test_results = 'Результаты тестов'

    def __init__(self, surname: str, name: str, name_father: str):
        self.surname = surname
        self.name = name
        self.name_father = name_father
        self.__grade_book = dict()
        if path.exists(FILE_NAME_CSV):
            with open(FILE_NAME_CSV, 'r', encoding='utf-8', newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter="\n")
                for row in csv_reader:
                    self.__grade_book[str(*row)] = {self.__grades: [], self.__test_results: []}
        else:
            raise FileExistsError(f'Ошибка! Файл "{FILE_NAME_CSV}" не найден!')

    def __str__(self):
        """
        Строковое представление объекта Студент
        """
        return f'{self.surname} {self.name} {self.name_father}'

    def __repr__(self):
        return f'Student: surname="{self.surname}", name="{self.name}",  name_father="{self.name_father}"\n' \
               f'grade_book: {self.__grade_book}'

    def print_list_grades(self, subject: str):
        """
        Метод печати списка оценок по какому-либо предмету
        :param subject: название предмета (строка)
        """
        if self.is_subject_in_grade_book(subject):
            list_grades = self.__grade_book[subject][self.__grades]
            print(f'{self}: оценки по предмету "{subject}" => {list_grades}')

    def print_list_tests(self, subject: str):
        """
        Метод печати списка результатов тестирования по какому-либо предмету
        :param subject: название предмета (строка)
        """
        if self.is_subject_in_grade_book(subject):
            list_tests = self.__grade_book[subject][self.__test_results]
            print(f'{self}: результаты тестирования по предмету "{subject}" => {list_tests}')

    def print_grade_book(self):
        """
        Метод печати журнала успеваемости объекта Студент
        """
        print(f'{HEADER_GRADE_BOOK}: {self}')
        for k, v in self.__grade_book.items():
            print(k.upper())
            for k1, v1 in v.items():
                print(f'\t{k1.upper()}: {v1}')

    def is_subject_in_grade_book(self, subject: str):
        """
        Метод проверки существования предмета в журнале оценок объекта Студент
        :param subject: название предмета (строка)
        """
        if subject not in self.__grade_book.keys():
            raise NameSubjectError(subject)
        return True

    def add_grade(self, subject: str, grade: int):
        """
        Метод добавления оценки объекту Студент
        :param subject: название предмета (строка)
        :param grade: количество баллов (целое число)
        """
        if grade not in range(MIN_GRADE, MAX_GRADE + 1):
            raise StudentGradeError(grade)
        if self.is_subject_in_grade_book(subject):
            self.__grade_book[subject][self.__grades].append(grade)

    def add_test_result(self, subject: str, num_score: int):
        """
        Метод добавления объекту Студент результата теста
        :param subject: название предмета (строка)
        :param num_score: количество баллов (целое число)
        """
        if num_score not in range(MIN_TEST_SCORE, MAX_TEST_SCORE + 1):
            raise StudentTestResultError(num_score)
        if self.is_subject_in_grade_book(subject):
            self.__grade_book[subject][self.__test_results].append(num_score)

    def average_test_score(self, subject: str) -> int:
        """
        Метод подсчитывает средний балл по тестам для каждого предмета объекта Студент
        :param subject: название предмета (строка)
        """
        if self.is_subject_in_grade_book(subject):
            scores = self.__grade_book[subject][self.__test_results]
            return round(sum(scores) / len(scores)) if scores else 0

    def average_grade(self) -> int:
        """
        Метод подсчитывает средний балл по оценкам всех предметов вместе взятых объекта Студент
        """
        total_grades = [grade for subj in self.__grade_book.values() for grade in subj[self.__grades]]
        return round(sum(total_grades) / len(total_grades)) if total_grades else 0


if __name__ == '__main__':
    student_1 = Student('Иванов', 'Петр', 'Олегович')
    print(student_1)
    student_1.add_grade('алгебра', 5)
    student_1.add_grade('химия', 4)
    student_1.add_grade('геометрия', 5)
    student_1.add_grade('литература', 4)
    student_1.add_grade('алгебра', 4)
    student_1.add_grade('биология', 5)
    student_1.print_list_grades('алгебра')
    student_1.print_list_grades('химия')
    student_1.print_list_grades('геометрия')
    student_1.print_list_grades('литература')
    student_1.print_list_grades('биология')
    student_1.add_test_result('алгебра', 100)
    student_1.add_test_result('геометрия', 75)
    student_1.add_test_result('геометрия', 0)
    student_1.add_test_result('литература', 100)
    student_1.add_test_result('алгебра', 69)
    student_1.add_test_result('литература', 95)
    student_1.add_test_result('география', 100)
    student_1.print_list_tests('алгебра')
    student_1.print_list_tests('геометрия')
    student_1.print_list_tests('литература')
    student_1.print_list_tests('география')
    average_test = student_1.average_test_score('алгебра')
    print(f'Средний балл за тестирование по алгебре составил: {average_test}')
    average_grades = student_1.average_grade()
    print(f'Средний балл оценок по всем предметам составил: {average_grades}')
