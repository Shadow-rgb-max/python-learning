def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Контакт {name} добавлен.")

def find_contact(contacts, name):
    return contacts.get(name, "Контакт не найден.")

def main():
    contacts = {}
    while True:
        action = input("Выберите действие: добавить контакт (д), найти контакт (н), выйти (в): ").lower()
        if action == 'д':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_contact(contacts, name, phone)
        elif action == 'н':
            name = input("Введите имя для поиска: ")
            result = find_contact(contacts, name)
            print(result)
        elif action == 'в':
            break
        else:
            print("Недопустимое действие. Попробуйте снова.")

if __name__ == "__main__":
    main()