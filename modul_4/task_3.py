import os # Модуль для работы с файловой системой
import sys # Модуль для работы с аргументами командной строки
from colorama import init, Fore # Модуль для работы с цветным выводом в консоли

# Получаем список всех файлов и папок в указанной директории
def print_directory_tree(root_dir, indent=""): 

# Сортируем список по алфавиту.
    entries = sorted(os.listdir(root_dir))

# Проходим по каждому элементу в списке
    for i, entry in enumerate(entries):
# Строим полный путь к текущему файлу/папке
        path = os.path.join(root_dir, entry)

# Определяем, какой префикс использовать: если это последний элемент в списке, используем └── (папка или файл в конце дерева).В остальных случаях используем ├──.
        prefix = "└── " if i == len(entries) - 1 else "├── "
# Если текущий элемент — папка, то он будет окрашен в синий цвет, если файл — в зелёный.
        color = Fore.BLUE if os.path.isdir(path) else Fore.GREEN
        print(indent + color + prefix + entry + Fore.RESET)
        if os.path.isdir(path):
            print_directory_tree(path, indent + ("    " if i == len(entries) - 1 else "│   "))

if __name__ == "__main__":
    init(autoreset=True)
# Проверяем, передан ли аргумент командной строки
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: Не вказано шлях до директорії!" + Fore.RESET)
        sys.exit(1)

# Получаем путь к директории из первого аргумента командной строки
    directory = sys.argv[1]
# Проверяем, существует ли такая директория. Если нет, выводим ошибку и завершаем выполнение программы
    if not os.path.isdir(directory):
        print(Fore.RED + "Помилка: Вказаний шлях не є директорією!" + Fore.RESET)
        sys.exit(1)
    
# Выводим путь к директории сине-зеленым цветом
    print(Fore.CYAN + directory + Fore.RESET)
# Вызываем функцию, чтобы вывести структуру файлов и папок внутри указанной директории
    print_directory_tree(directory)
