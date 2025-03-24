def parse_input(user_input):
# Ця функція приймає рядок вводу користувача user_input і розбиває його на слова, використовуючи пробіл як розділювач
    cmd, *args = user_input.split()

# Бот не чутливий до регістру введених команд (видаляє зайві пробіли навколо команди та перетворює її на нижній регістр)
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція призначена для додавання нового контакту до словника контактів
def add_contact(args, contacts):
# якщо args не містить двох елементів, ця функція викличе помилку
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone."
    name, phone = args
    contacts[name] = phone
# Функція повертає рядок, що підтверджує успішне додавання контакту
    return "Contact added."

# Функція призначена змінювати записаний номер телефону
def change_contact(args, contacts):
# якщо контакт не знайдено, виводиться відповідне повідомлення.
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# бот виводить номер телефону для конкретного контакту
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

# бот виводить всі збережені контакти
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
# словник з контактами
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

# "close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!"
        if command in ["close", "exit"]:
            print("Good bye!")
            break

# Бот приймає команду: "hello", та відповідає у консоль повідомленням "How can I help you?"
        elif command == "hello":
            print("How can I help you?")

# Бот приймає команду: "add username phone" - зберігає у пам'яті у словнику, новий контакт
        elif command == "add":
            print(add_contact(args, contacts))

# Бот приймає команду: "change username phone" - бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику
        elif command == "change":
            print(change_contact(args, contacts))

# Бот приймає команду: "phone username" - бот виводить у консоль номер телефону для зазначеного контакту username
        elif command == "phone":
            print(show_phone(args, contacts))

# Бот приймає команду: "all" -  За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
