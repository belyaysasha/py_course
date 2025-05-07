class BadPriorityError(Exception):
    """Исключение возникает при создании задачи с приоритетом меньше 0."""
    
    def __init__(self, message="Приоритет задачи не может быть отрицательным."):
        super().__init__(message)


class BadIdError(Exception):
    """Исключение возникает при создании задачи с id меньше 0 и/или больше 1000000."""
    
    def __init__(self, message="ID задачи должен быть в диапазоне от 0 до 1000000."):
        super().__init__(message)


class BadNameError(Exception):
    """Исключение возникает при создании задачи с именем меньше 7 символов."""
    
    def __init__(self, message="Имя задачи должно содержать не менее 7 символов."):
        super().__init__(message)