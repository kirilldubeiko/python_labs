"""Иерархия исключений."""

class AppError(Exception):
    """Базовая ошибка приложения."""
    pass

class ValidationError(AppError):
    """Ошибка валидации."""
    pass

class StudentNotFoundError(AppError):
    """Студент не найден."""
    pass

class CSVFormatError(AppError):
    """Ошибка с csv."""
    pass

class DuplicateIdError(AppError):
    """Айди повторяется."""
    pass




