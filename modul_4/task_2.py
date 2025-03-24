from pathlib import Path
# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
def get_cats_info(path):
    cats_info = []
    
    file_path = Path(__file__).parent/path
    if not file_path.exists():
        print(f"Файл '{path}' не знайдено.")
        return cats_info
    
    try:
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cats_info.append({"id": cat_id, "name": name, "age": age,})
                    else:
                        print(f"Пропущено некоректний рядок: {line}")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
 # Функція має повертати список словників, де кожен словник містить інформацію про одного кота.   
    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

