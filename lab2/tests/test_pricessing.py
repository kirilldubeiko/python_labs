import pytest
from lab.models import Student
from lab.processing import (
    sort_students, count_students, count_group_statistics,
    add_student, delete_by_id,
)
from lab.errors import DuplicateIdError, StudentNotFoundError


def test_sort_by_avg():
    students = [
        Student(1, "А", [50]),
        Student(2, "Б", [90]),
    ]
    assert sort_students(students, "avg")[0].full_name == "Б"


def test_count():
    assert count_students([]) == 0
    assert count_students([Student(1, "А", [])]) == 1


def test_statistics_empty():
    stats = count_group_statistics([])
    assert stats["count"] == 0
    assert stats["overall_avg"] == 0.0


def test_add_student():
    students = []
    add_student(students, Student(1, "А", []))
    assert len(students) == 1


def test_duplicate_id():
    students = [Student(1, "А", [])]
    with pytest.raises(DuplicateIdError):
        add_student(students, Student(1, "Б", []))


def test_delete_by_id():
    students = [Student(1, "А", []), Student(2, "Б", [])]
    delete_by_id(students, 1)
    assert len(students) == 1


def test_delete_not_found():
    with pytest.raises(StudentNotFoundError):
        delete_by_id([], 999)