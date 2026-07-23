import re
import json
from datetime import datetime
import os
CONTACTS_FILE = 'contacts.json'

class Contact:
    def __init__(self, name : str, phone : str, updated_on : str):
        self.name = name
        self.phone = phone
        self.updated_on = updated_on

    def __str__(self) -> str:
        return f"Имя: {self.name}, Номер телефона: {self.phone}, Последнее обновление: {self.updated_on}"
    
    def update_phone(self, new_phone):
        self.phone = new_phone
        self.updated_on = datetime.now().strftime('%d.%m.%Y %H:%M')

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        pattern = r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$'
        return re.match(pattern, phone) is not None

class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def __str__(self):
        return "class phonebook"
    
    def load(self, filename=CONTACTS_FILE):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.contacts = {name: Contact(name, item['phone'], item['updated_on']) for name, item in data.items()}

    def save(self, filename=CONTACTS_FILE):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({name: contact.__dict__ for name, contact in self.contacts.items()}, f, ensure_ascii=False, indent=2)

    def add(self, name: str, phone: str):
        if not self.find(name):
            if not Contact.is_valid_phone(phone):
                raise ValueError('неверный формат номера телефона')
            self.contacts[name] = Contact(name, phone, datetime.now().isoformat())
            self.save()
            return True
        return False
    
    def delete(self, name: str) -> bool:
        if name in self.contacts:
            del self.contacts[name]
            self.save()
            return True
        return False
    
    def edit(self, name: str, new_phone: str) -> bool:
        if name in self.contacts:
            if not Contact.is_valid_phone(phone):
                raise ValueError("Неверный формат номера телефона.")
            self.contacts[name] = Contact.update_phone(new_phone)
            self.save()
            return True
        return False
    
    def find(self, name: str) -> dict[str, dict[str, ...]]:
        return self.contacts.get(name)
    
