from to_do_list import Task, ToDoList
from exceptions import BadPriorityError, BadIdError, BadNameError

def main():
    """Основная функция для взаимодействия с пользователем и управления списком задач."""
    
    todo_list = ToDoList()  # Создаем новый список задач

    while True:
        print("\nTo Do List")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Показать задачи")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            try:
                # Запрос данных о задаче у пользователя
                task_id = int(input("Введите ID задачи (0-1000000): "))
                name = input("Введите имя задачи (минимум 7 символов): ")
                priority = int(input("Введите приоритет задачи (неотрицательное число): "))
                
                # Создаем новую задачу и добавляем ее в список
                task = Task(task_id, name, priority)
                todo_list.add_task(task)
                print("Задача добавлена.")
                
            except (BadIdError, BadNameError, BadPriorityError) as e:
                # Обработка исключений и вывод сообщения об ошибке
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                # Запрос ID задачи для удаления
                task_id = int(input("Введите ID задачи для удаления: "))
                todo_list.remove_task(task_id)
                print("Задача удалена.")
                
            except Exception as e:
                # Обработка возможных ошибок при удалении
                print(f"Ошибка: {e}")

        elif choice == '3':
            # Вывод списка задач
            print("Список задач:")
            print(todo_list)

        elif choice == '4':
            print("Выход из программы.")
            break  # Завершение программы

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()  # Запуск основной функции