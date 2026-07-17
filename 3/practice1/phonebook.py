# phonebook.py
import os
import json
from datetime import datetime
import re

CONTACTS_FILE = "contacts.json"

def save(contacts, filename=CONTACTS_FILE):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def load(filename=CONTACTS_FILE):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def check_phone_number(phone):
    # Проверка формата номера телефона (например, +7 123 456-78-90)
    pattern = r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$'
    return re.match(pattern, phone) is not None

def add_contact(contacts, name, phone):
    contacts[name] = {
        "phone": phone,
        "updated_on": datetime.now().isoformat()
    }
    save(contacts)
    return True

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save(contacts)
        return True
    return False

def edit_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = {
            "phone": new_phone,
            "updated_on": datetime.now().isoformat()
        }
        save(contacts)
        return True
    return False

def find_contact(contacts, name):
    return contacts.get(name)  # None, если не найден

