from pathlib import Path

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
def total_salary(path):
    try:
        path = Path(path)  # Перетворюємо шлях у Path-об'єкт
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1].strip())  # Очищаємо пробіли та Використовуємо float
                        salaries.append(salary)
                    except ValueError:
                        print(f"Помилка у рядку: {line.strip()} - некоректний формат зарплати.")

        if not salaries:
            return (0, 0)  # Якщо немає даних, повертаємо (0, 0)
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
        total = sum(salaries)
        average = total / len(salaries) if salaries else 0.0  # Уникаємо ділення на 0
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
        return (total, average)

    except FileNotFoundError:
        print("Файл відсутній.")
        return (0, 0)
    except Exception as e:
        print(f"файл пошкоджений.: {e}")
        return (0, 0)

total, average = total_salary("c:/Users/User/Projects/vscode/modul_4/salary-file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
