from phonebook import PhoneBook

def main():
    phonebook = PhoneBook()
    phonebook.load()
    
    while True:
        action = input("Выберите действие: добавить контакт (д), найти контакт (н), удалить контакт (у), редактировать контакт (р), выйти (в): ").lower()
        if action == 'д':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            try:
                if phonebook.add(name, phone):
                    print(f"Контакт {name} добавлен.")
                else:
                    print("Контакт с таким именем уже существует.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif action == 'н':
            name = input("Введите имя для поиска: ")
            contact = phonebook.find(name)
            if contact:
                print(f"Результат:\n {contact}")
            else:
                print("Контакт не найден.")
        elif action == 'у':
            name = input("Введите имя для удаления: ")
            if phonebook.delete(name):
                print(f"Контакт {name} удален.")
            else:
                print("Контакт не найден.")
        elif action == 'р':
            name = input("Введите имя для редактирования: ")
            new_phone = input("Введите новый номер телефона: ")
            try:
                if phonebook.edit(name, new_phone):
                    print(f"Контакт {name} обновлен.")
                else:
                    print("Контакт не найден.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif action == 'в':
            break
        else:
            print("Недопустимое действие. Попробуйте снова.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
