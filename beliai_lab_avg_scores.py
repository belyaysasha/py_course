def is_valid_name(name):
    """
    Проверяет, является ли имя допустимым.
    
    :param name: Имя студента.
    :return: True, если имя допустимо; иначе False.
    """
    return len(name) >= 2 and name.isalpha()

def is_valid_score(score):
    """
    Проверяет, является ли оценка допустимой.
    
    :param score: Оценка студента.
    :return: True, если оценка в пределах от 1 до 10; иначе False.
    """
    return 1 <= score <= 10

def add_student(scores):
    """
    Добавляет студента и его оценку в словарь.
    
    :param scores: Словарь с именами студентов и их оценками.
    """
    name = input("Введите имя студента: ").strip()
    
    if not is_valid_name(name):
        print("Недопустимое имя. Имя должно содержать не менее двух букв и не содержать цифр.")
        return
    
    score = input(f"Введите оценку для {name} (от 1 до 10): ").strip()
    
    try:
        score = float(score)
        if not is_valid_score(score):
            print("Недопустимая оценка. Оценка должна быть от 1 до 10.")
            return
    except ValueError:
        print("Ошибка: Ввод должен быть числом.")
        return
    
    if name in scores:
        scores[name].append(score)
    else:
        scores[name] = [score]

def remove_student(scores):
    """
    Удаляет студента из словаря.
    
    :param scores: Словарь с именами студентов и их оценками.
    """
    name = input("Введите имя студента для удаления: ").strip()
    
    if name in scores:
        del scores[name]
        print(f"Студент {name} удален.")
    else:
        print(f"Студент {name} не найден.")

def calculate_average_scores(scores):
    """
    Вычисляет и выводит средний балл для каждого студента.
    
    :param scores: Словарь с именами студентов и их оценками.
    """
    for name, score_list in scores.items():
        average_score = sum(score_list) / len(score_list)
        print(f"{name}: Средний балл = {average_score:.2f}")