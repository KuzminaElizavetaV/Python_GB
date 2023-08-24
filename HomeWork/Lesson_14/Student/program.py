from student import Student
from student_exceptions import StudentNameError
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='students.log', encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def run_from_console():
    parser = argparse.ArgumentParser(prog='create_student',
                                     description='Создает объект типа Student',
                                     epilog='Запуск из консоли: python student.py -s Шарапова -n Светлана -f Федоровна')
    parser.add_argument('-s', '--surname', type=str, help='Фамилия')
    parser.add_argument('-n', '--name', type=str, help='Имя')
    parser.add_argument('-f', '--father_name', type=str, help='Отчество')
    args = parser.parse_args()
    return create_student(args.surname, args.name, args.father_name)


def create_student(surname: str, name: str, name_father: str) -> Student | None:
    try:
        student = Student(surname, name, name_father)
        log_msg = f'Студент <<{student}>> успешно создан'
        print(log_msg)
        logger.info(log_msg)
    except StudentNameError:
        log_msg = f'Нельзя создать студента с именем <<{surname} {name} {name_father}>>. ' \
                  f'ФИО должно содержать только буквы и начинаться с заглавной буквы'
        print(log_msg)
        logger.error(log_msg)
        return None
    return student


if __name__ == '__main__':
    print(run_from_console())
