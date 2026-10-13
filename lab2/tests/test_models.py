import pytest
from lab.models import Student
from lab.errors import ValidationError


def test_create_student():
    s = Student(1, "Иван", [78, 85, 90])
    assert s.student_id == 1
    assert s.full_name == "Иван"
    assert s.grade_list == [78, 85, 90]


def test_average_grade():
    s = Student(1, "Иван", [80, 90])
    assert s.average_grade == pytest.approx(85.0)


def test_empty_grades():
    assert Student(1, "Иван", []).average_grade == 0.0


def test_invalid_id():
    with pytest.raises(ValidationError):
        Student(-1, "Иван", [])