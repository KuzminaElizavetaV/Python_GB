__all__ = ['StudentNameError', 'NameSubjectError', 'StudentGradeError', 'StudentTestResultError']


class StudentNameError(ValueError):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Нельзя создать объект с таким именем, отчеством или фамилией: "{self.name}". ' \
               f'ФИО должно содержать только буквы и начинаться с заглавной буквы'


class NameSubjectError(KeyError):
    def __init__(self, subject: str):
        self.subject = subject

    def __str__(self):
        return f'Предмет "{self.subject}" отсутствует в журнале оценок студента!'


class StudentGradeError(ValueError):
    def __init__(self, grade: int):
        self.grade = grade

    def __str__(self):
        return f'Нельзя поставить студенту оценку {self.grade} баллов по предмету. Значение "{self.grade}" ' \
               f'выходит за рамки диапазона, который варьируется от 2 до 5 баллов включительно!'


class StudentTestResultError(ValueError):
    def __init__(self, num_score: int):
        self.num_score = num_score

    def __str__(self):
        return f'Нельзя поставить студенту {self.num_score} баллов за тест. Значение "{self.num_score}" ' \
               f'выходит за рамки диапазона, который варьируется от 0 до 100 баллов включительно!'
