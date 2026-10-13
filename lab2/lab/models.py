from lab.errors import ValidationError

class Student:
    """Модель студента, поля id, full_name, grade_list."""
    def __init__(self, student_id: int, full_name: str, grade_list: list[int|None] = None):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValidationError(f'Некорректный id:{student_id}.')
        if not isinstance(full_name, str) or not full_name.strip():
            raise ValidationError(f'Некорректное ФИО:{full_name}')
        self.student_id = student_id
        self.full_name = full_name.strip()
        if grade_list is None:
            self.grade_list = []
        else:
            self.grade_list = grade_list
        for i in range(len(self.grade_list)):
            if self.grade_list[i] is None:
                continue
            if not isinstance(self.grade_list[i], int) or not 0 <= self.grade_list[i] <= 100:
                raise ValidationError(f"Некорректная оценка{self.grade_list[i]}")

    @property
    def average_grade(self) -> float:
        """Считает среднее арифметическое оценок студента."""
        grade_sum = 0
        none_counter = 0
        if len(self.grade_list) == self.grade_list.count(None):
            return 0.0
        else:
            for i in range(len(self.grade_list)):
                if self.grade_list[i] is not None:
                    grade_sum += self.grade_list[i]
                else:
                    none_counter += 1
            return grade_sum / (len(self.grade_list) - none_counter)




