"""Содержит функции для работы с csv."""

import csv
from lab.models import *
from lab.processing import *

def load_students(path: str, has_header: bool =True) -> list[Student]:
    """Загружает студентов из csv-файла."""
    students = []
    try:
        with open(path, encoding="utf-8", newline="") as csvfile:
            reader = csv.reader(csvfile)
            if has_header:
                header = next(reader)
            for row in reader:
                grades = []
                for i in range(len(row) - 2):
                    grades.append(int(row[i + 2]) if row[i + 2] else None)
                students.append(Student(int(row[0]), row[1], grades))
        return students
    except OSError as e:
        raise CSVFormatError(f"Не удалось прочитать файл: {e}")


def save_students(path: str, students: list[Student], has_header: bool =True) -> None:
    """Сохраняет студентов в csv-файл."""
    try:
        with open(path, 'w', encoding="utf-8", newline="") as csvfile:
            max_grade_count = max((len(student.grade_list) for student in students), default=0)
            writer = csv.writer(csvfile)
            if has_header:
                writer.writerow(['id','name'] + [f'grade{i+1}' for i in range(max_grade_count)])
            for student in students:
                row = [student.student_id, student.full_name]
                for i in range(max_grade_count):
                    if i < len(student.grade_list) and student.grade_list[i] is not None:
                        row.append(student.grade_list[i])
                    else:
                        row.append('')
                writer.writerow(row)
    except OSError as e:
        raise CSVFormatError(f"Не удалось записать файл: {e}")

def export_top_n(path: str, students: list[Student], n: int) -> None:
    """Сохраняет в csv-файл топ n лучших студентов."""
    try:
        with open(path, 'w', encoding="utf-8", newline="") as csvfile:
            writer = csv.writer((csvfile))
            writer.writerow(['id','name','average','grades'])
            sorted_students = sort_students(students)
            for s in sorted_students[:n]:
                writer.writerow([s.student_id, s.full_name, s.average_grade, " ".join( str(grade) if grade is not None else "" for grade in s.grade_list)])
    except OSError as e:
        raise CSVFormatError(f"Не удалось записать файл: {e}")