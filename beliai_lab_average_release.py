from beliai_lab_avg_scores import *  # Импортируем все функции из scores.py

def main():
    scores = {}  # Словарь для хранения оценок студентов

    while True:
        action = input("Введите 'add' для добавления студента, 'remove' для удаления студента или 'exit' для выхода: ").strip().lower()
        
        if action == 'add':
            add_student(scores)
        elif action == 'remove':
            remove_student(scores)
        elif action == 'exit':
            break
        else:
            print("Недопустимое действие. Пожалуйста, попробуйте снова.")

    print("\nСредние баллы студентов:")
    calculate_average_scores(scores)

if __name__ == "__main__":
    main()