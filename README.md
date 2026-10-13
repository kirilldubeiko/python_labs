# Лабораторная работа 2

Управление студентами и оценками через CSV.

## Запуск

python -m lab.main

## Тесты

python -m pytest -q

## Структура

- `lab/errors.py` — иерархия исключений
- `lab/models.py` — класс Student
- `lab/io_utils.py` — работа с CSV
- `lab/processing.py` — сортировка, статистика
- `lab/main.py` — CLI-меню
- `data/students.csv` — пример данных
- `tests/` — 16 автотестов pytest

## Основные функции

- `load_students(path, has_header=True)` — загрузка
- `save_students(path, students, has_header=True)` — сохранение
- `export_top_n(path, students, n)` — ТОП-N
- `sort_students(students, key)` — сортировка avg/name/id
- `count_group_statistics(students)` — статистика
