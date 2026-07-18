from datetime import datetime
import re
import os
import json

CONTACTS_FILE = "contacts.json"

class Contact:
    def __init__(self, name, phone, updated_on):
        self.name = name
        self.phone = phone
        self.updated_on = updated_on
    
    def __str__(self):
        return f"Имя: {self.name}, Номер телефона: {self.phone}, Последнее обновление: {self.updated_on}"
    
    def __dict__(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "updated_on": self.updated_on
        }
    
    def update_phone(self, new_phone):
        self.phone = new_phone
        self.updated_on = datetime.now().isoformat()
        
class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def save(self, filename=CONTACTS_FILE):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({name: contact.__dict__ for name, contact in self.contacts.items()}, f, ensure_ascii=False, indent=2)

    def load(self, filename=CONTACTS_FILE):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.contacts = {name: Contact(name, info['phone'], info['updated_on']) for name, info in data.items()}
    
    def add(self, name, phone):
        if not self.find(name):
            self.contacts[name] = Contact(name, phone, datetime.now().isoformat())
            return True
        return False

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False
    
    def edit(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name].update_phone(new_phone)
            return True
        return False
    
    def find(self, name):
        return self.contacts.get(name)  # None, если не найден
