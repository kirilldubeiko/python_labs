import csv
from lab.models import *
from lab.processing import *

def load_students(path):
    students = []
    with open(path, encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grades = []
            for key, value in row.items():
                if key.startswith('grade'):
                    grades.append(int(value)) if value else grades.append(None)
            students.append(Student(int(row['id']),row['name'], grades))
    return students

def save_students(path, students):
    with open(path, 'w', encoding="utf-8", newline="") as csvfile:
        max_grade_count = max((len(student.grade_list) for student in students), default=0)
        writer = csv.writer(csvfile)
        writer.writerow(['id','name'] + [f'grade{i+1}' for i in range(max_grade_count)])
        for student in students:
            row = [student.student_id, student.full_name]
            for i in range(max_grade_count):
                if i < len(student.grade_list) and student.grade_list[i] is not None:
                    row.append(student.grade_list[i])
                else:
                    row.append('')
            writer.writerow(row)

def export_top_n(path, students, n):
    with open(path, 'w', encoding="utf-8", newline="") as csvfile:
        writer = csv.writer((csvfile))
        writer.writerow(['id','name','average','grades'])
        sorted_students = sort_students(students)
        for s in sorted_students[:n]:
            writer.writerow([s.student_id, s.full_name, s.average_grade, " ".join( str(grade) if grade is not None else "" for grade in s.grade_list)])