phone_book = {}
while True:
    name = input("Введите имя для добавления в телефонную книгу (или 'стоп' для завершения): ")
    if name.lower() == 'стоп':
        break
    phone_number = input(f"Введите номер телефона для {name}: ")
    phone_book[name] = phone_number

name_to_lookup = input("Введите имя для поиска в телефонной книге: ")
if name_to_lookup in phone_book:
    print(f"Номер телефона для {name_to_lookup}: {phone_book[name_to_lookup]}")
else:
    print(f"Контакт{name_to_lookup} не найден в телефонной книге.")