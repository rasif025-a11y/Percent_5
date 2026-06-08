import random

def generate_task():

    task_type = random.randint(1, 5)

    # 1. Найти процент от числа
    if task_type == 1:
        number = random.randint(100, 900)
        percent = random.choice([5, 10, 15, 20, 25, 30, 40, 50])

        question = f"Найдите {percent}% от числа {number}"
        answer = number * percent / 100

    # 2. Найти число по проценту
    elif task_type == 2:
        number = random.randint(100, 500)
        percent = random.choice([10, 20, 25, 50])

        part = number * percent / 100

        question = f"{part} составляет {percent}% какого числа?"
        answer = number

    # 3. Найти процентное отношение
    elif task_type == 3:
        a = random.randint(10, 90)
        b = a * random.choice([2, 4, 5])

        question = f"Сколько процентов составляет {a} от {b}?"
        answer = a / b * 100

    # 4. Увеличение на процент
    elif task_type == 4:
        number = random.randint(100, 500)
        percent = random.choice([10, 20, 30])

        question = f"Увеличьте {number} на {percent}%"
        answer = number * (1 + percent / 100)

    # 5. Уменьшение на процент
    else:
        number = random.randint(100, 500)
        percent = random.choice([10, 20, 30])

        question = f"Уменьшите {number} на {percent}%"
        answer = number * (1 - percent / 100)

    return question, answer