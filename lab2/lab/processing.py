"""Функции обработки студентов."""
from lab.models import *
from lab.errors import *
def sort_students(students: list[Student], key: str = "avg") -> list[Student]:
    """Сортировка студентов по ключам : avg, name, id."""
    if key == 'avg':
        return sorted(students, key=lambda s:(-s.average_grade, s.full_name))
    elif key == 'name':
        return sorted(students, key=lambda s:s.full_name)
    elif key == 'id':
        return sorted(students, key=lambda s:s.student_id)
    else:
        raise ValidationError(f"Неизвестный ключ сортировки: {key}")

def count_students(students: list[Student]) -> int:
    """Считает студентов."""
    return len(students)

def find_best_student(students: list[Student]) -> Student:
    """Находит лучшего студента."""
    if not students:
        return None
    return max(students, key=lambda s:s.average_grade)

def find_worst_student(students: list[Student]) -> Student:
    """Находит худшего студента."""
    if not students:
        return None
    return min(students, key=lambda s:s.average_grade)

def add_student(students: list[Student], student: Student) -> None:
    """Добавляет студента."""
    if any(student.student_id == s.student_id for s in students):
        raise DuplicateIdError(f"id={student.student_id} уже занят")
    students.append(student)

def find_by_id(students: list[Student], student_id: int) -> Student:
    """Находит студента по id."""
    for student in students:
        if student.student_id == student_id:
            return student
    raise StudentNotFoundError(f"Студент id={student_id} не найден")

def delete_by_id(students: list[Student], student_id: int) -> None:
    """Удаляет студента по id."""
    students.remove(find_by_id(students,student_id))

def overall_grade(students: list[Student]) -> int:
    """Среднее арифметическое всех оценок."""
    all_grades = [grade for student in students for grade in student.grade_list if grade is not None]
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0.0

def count_group_statistics(students: list[Student]) -> dict:
    """Статистика группы."""
    return {
        'count':count_students(students),
        'overall_avg':overall_grade(students),
        'best':find_best_student(students),
        'worst':find_worst_student(students),
    }
