from lab.models import Student
from lab.io_utils import load_students, save_students


def test_roundtrip(tmp_path):
    students = [
        Student(1, "Иван", [78, 85]),
        Student(2, "Пётр", [90]),
    ]

    path = tmp_path / "students.csv"

    save_students(path, students)
    loaded = load_students(path)

    assert len(loaded) == 2
    assert loaded[0].student_id == 1
    assert loaded[0].full_name == "Иван"
    assert loaded[0].grade_list == [78, 85]
    assert loaded[1].student_id == 2
    assert loaded[1].full_name == "Пётр"
    assert loaded[1].grade_list == [90, None]