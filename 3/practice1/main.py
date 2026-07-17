from phonebook import add_contact, find_contact, delete_contact, edit_contact, load, check_phone_number

def main():
    contacts = load()
    while True:
        action = input("Выберите действие: добавить контакт (д), найти контакт (н), удалить контакт (у), редактировать контакт (р), выйти (в): ").lower()
        if action == 'д':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            if check_phone_number(phone):
                add_contact(contacts, name, phone)
                print(f"Контакт {name} добавлен.")
            else:
                print("Неверный формат номера телефона.")
        elif action == 'н':
            name = input("Введите имя для поиска: ")
            data = find_contact(contacts, name)
            if data:
                result = f"Имя: {name}, Номер телефона: {data['phone']}, Последнее обновление: {data['updated_on']}"
                print(f"Результат:\n {result}")
            else:
                print("Контакт не найден.")

        elif action == 'у':
            name = input("Введите имя для удаления: ")
            if delete_contact(contacts, name):
                print(f"Контакт {name} удален.")
            else:
                print("Контакт не найден.")
        elif action == 'р':
            name = input("Введите имя для редактирования: ")
            new_phone = input("Введите новый номер телефона: ")
            if check_phone_number(new_phone):
                if edit_contact(contacts, name, new_phone):
                    print(f"Контакт {name} обновлен.")
                else:
                    print("Контакт не найден.")
            else:
                print("Неверный формат номера телефона.")
        elif action == 'в':
            break
        else:
            print("Недопустимое действие. Попробуйте снова.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")