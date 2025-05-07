from exceptions import BadPriorityError, BadIdError, BadNameError

class Task:
    """Класс, представляющий задачу в списке дел."""
    
    def __init__(self, task_id: int, name: str, priority: int):
        """
        Инициализация задачи.
        
        task_id: уникальный идентификатор задачи (должен быть от 0 до 1000000)
        name: название задачи (должно содержать не менее 7 символов)
        priority: приоритет задачи (не должен быть отрицательным)
        BadIdError: если task_id вне допустимого диапазона
        BadNameError: если имя задачи короче 7 символов
        BadPriorityError: если приоритет отрицательный
        """
        if not (0 <= task_id <= 1000000):
            raise BadIdError()
        if len(name) < 7:
            raise BadNameError()
        if priority < 0:
            raise BadPriorityError()

        self.task_id = task_id
        self.name = name
        self.priority = priority

    def __str__(self):
        """Возвращает строковое представление задачи."""
        return f"Task(ID: {self.task_id}, Name: {self.name}, Priority: {self.priority})"


class ToDoList:
    """Класс, представляющий список задач."""
    
    def __init__(self):
        """Инициализация пустого списка задач."""
        self.tasks = []

    def add_task(self, task: Task):
        """
        Добавляет задачу в список.
        
        task: задача, которую нужно добавить
        """
        self.tasks.append(task)

    def remove_task(self, task_id: int):
        """
        Удаляет задачу из списка по ее идентификатору.
        
        task_id: идентификатор задачи, которую нужно удалить
        """
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def list_tasks(self):
        """
        Возвращает отсортированный список задач по приоритету.
        
        return: список задач, отсортированных по приоритету
        """
        return sorted(self.tasks, key=lambda x: x.priority)

    def __str__(self):
        """Возвращает строковое представление списка задач."""
        return "\n".join(str(task) for task in self.list_tasks())