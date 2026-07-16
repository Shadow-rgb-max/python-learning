from phonebook import add_contact, find_contact, delete_contact, edit_contact

def main():
    contacts = {}
    while True:
        action = input("Выберите действие: добавить контакт (д), найти контакт (н), удалить контакт (у), редактировать контакт (р), выйти (в): ").lower()
        if action == 'д':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_contact(contacts, name, phone)
            print(f"Контакт {name} добавлен.")
        elif action == 'н':
            name = input("Введите имя для поиска: ")
            result = find_contact(contacts, name)
            print(f"Результат: {result}")

        elif action == 'у':
            name = input("Введите имя для удаления: ")
            if delete_contact(contacts, name):
                print(f"Контакт {name} удален.")
            else:
                print("Контакт не найден.")
        elif action == 'р':
            name = input("Введите имя для редактирования: ")
            new_phone = input("Введите новый номер телефона: ")
            if edit_contact(contacts, name, new_phone):
                print(f"Контакт {name} обновлен.")
            else:
                print("Контакт не найден.")
        elif action == 'в':
            break
        else:
            print("Недопустимое действие. Попробуйте снова.")

if __name__ == "__main__":
    main()