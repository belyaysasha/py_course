def display_task_list(task_list):
    """
    Отображает список задач с их номерами, названиями и приоритетами.
    
    :param task_list: Список задач, где каждая задача представлена как строка.
    """
    if not task_list:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for task in task_list:
            print(task)


def display_cond_list(task_list):
    """
    Форматирует список задач в виде строки.
    
    :param task_list: Список задач, где каждая задача представлена как строка.
    :return: Строка с задачами, разделенными новой строкой.
    """
    return "\n".join(task_list)


def enter_task(task_list):
    """
    Запрашивает у пользователя ввод задач и добавляет их в список.
    
    :param task_list: Список задач, куда будут добавляться новые задачи.
    """
    while True:
        user_input = input("Введите задачу (или 'stop' для выхода): ").strip()
        
        if user_input.lower() == "stop":
            break
        
        # Запрашиваем приоритет
        priority = input("Введите приоритет задачи (высокий, средний, низкий): ").strip().lower()
        
        # Формируем строку задачи
        task_number = len(task_list) + 1  # Номер задачи
        task_entry = f"{task_number}. {user_input} - Приоритет: {priority}"
        
        task_list.append(task_entry)
        print(f"Задача добавлена: {task_entry}")


def main():
    """
    Основная функция, управляющая программой To Do List.
    """
    task_list = []  # Инициализируем пустой список задач
    enter_task(task_list)  # Ввод задач от пользователя
    display_task_list(task_list)  # Отображаем все задачи после завершения ввода


if __name__ == "__main__":
    main()