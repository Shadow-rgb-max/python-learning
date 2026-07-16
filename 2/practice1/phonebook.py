# phonebook.py
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return True

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    return False

def edit_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return True
    return False

def find_contact(contacts, name):
    return contacts.get(name)  # None, если не найден