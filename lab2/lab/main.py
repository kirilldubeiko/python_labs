"""Функции меню."""
from lab.models import Student
from lab.io_utils import load_students, save_students, export_top_n
from lab.processing import (
    sort_students, count_students, overall_grade,
    find_best_student, find_worst_student, count_group_statistics,
    find_by_id, add_student, delete_by_id,
)
from lab.errors import *

def show_menu() -> None:
    """Показывает меню"""
    print("Меню")
    print("1. Загрузка из CSV")
    print("2. Сохранение в CSV")
    print("3. Показать всех")
    print("4. Добавить студента")
    print("5. Удалить по id")
    print("6. Обновить оценки")
    print("7. Статистика")
    print("8. Экспорт ТОП-N")
    print("9. Сортировка")
    print("0. Выход")

def show_all_students(students: list[Student]) -> None:
    """Выводит таблицу студентов"""
    if not students:
        print("Список пуст.")
        return
    else:
        print(f"{'id':<5} {'ФИО':<25} {'оценки':<20} {'средний':<8}")
        for s in students:
            grades = " ".join(str(g) if g is not None else "—" for g in s.grade_list)
            print(f"{s.student_id:<5} {s.full_name:<25} {grades:<20} {s.average_grade:<8.2f}")

def input_grades() -> list[int|None]:
    """Ввод оценок студента"""
    raw = input("Оценки через пробел(если оценки нет, то -): ").strip()
    if not raw:
        return []
    grades = []
    for part in raw.split():
        if part == "-":
            grades.append(None)
            continue
        try:
            g = int(part)
        except ValueError:
            raise ValidationError(f"Оценка не число: {part}")
        if not (0 <= g <= 100):
            raise ValidationError(f"Оценка вне диапазона от 0 до 100: {g}")
        grades.append(g)
    return grades

def input_id(prompt: str) -> int:
    """Возвращает айди студента"""
    student_id = input(prompt).strip()
    try:
        return int(student_id)
    except ValueError:
        raise ValidationError(f"id должен быть числом: {student_id}")

def main() -> None:
    """Работа с меню"""
    students = []
    while True:
        show_menu()
        choice = input("Введите пункт: ").strip()
        try:
            if choice == "1":
                students = load_students("data/students.csv")
                print(f"Загружено:{len(students)}")
            elif choice == "2":
                save_students("data/students.csv", students)
            elif choice == "3":
                show_all_students(students)
            elif choice == "4":
                new_id = input_id("Введите id нового студента: ")
                name = input("Введите ФИО: ").strip()
                grades = input_grades()
                add_student(students, Student(new_id, name, grades))
            elif choice == "5":
                new_id = input_id("Введите id студента: ")
                delete_by_id(students, new_id)
            elif choice == "6":
                student_id = input_id("Введите id студента: ")
                student = find_by_id(students, student_id)
                print(f"Текущие оценки: {student.grade_list}")
                student.grade_list = input_grades()
                print(f"Обновлено: {student.grade_list}")
            elif choice == "7":
                stats = count_group_statistics(students)
                print(f"\nСтудентов: {stats['count']}")
                print(f"Средний по всем оценкам: {stats['overall_avg']:.2f}")
                if stats["best"]:
                    print(f"Лучший: {stats['best'].full_name}")
                if stats["worst"]:
                    print(f"Худший: {stats['worst'].full_name}")
            elif choice == "8":
                if not students:
                    print("Список пуст.")
                    continue
                n = input_id("Введите количество студентов ")
                if n <= 0:
                    raise ValidationError("Количество студентов должно быть > 0")
                if n > len(students):
                    raise ValidationError(f"Количество студентов должно быть не > {len(students)}")
                export_top_n("data/top.csv", students, n)
            elif choice == "9":
                if not students:
                    print("Список пуст.")
                    continue
                key = input("Ключ (avg/name/id): ").strip() or "avg"
                show_all_students(sort_students(students, key))

            elif choice == "0":
                print("Программа завершена.")
                break
            else:
                print("Неверный пункт")
        except AppError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()







