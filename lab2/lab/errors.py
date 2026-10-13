class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class StudentNotFoundError(AppError):
    pass

class CSVFormatError(AppError):
    pass

class DuplicateIdError(AppError):
    pass




