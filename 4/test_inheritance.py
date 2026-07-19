from datetime import datetime


class Contact:
    def __init__(self, name, phone, updated_on):
        self.name = name
        self.phone = phone
        self.updated_on = updated_on
    
    def __str__(self):
        return f"Имя: {self.name}, Номер телефона: {self.phone}, Последнее обновление: {self.updated_on}"
    
    def update_phone(self, new_phone):
        self.phone = new_phone
        self.updated_on = datetime.now().isoformat()
    
    @staticmethod
    def is_valid_phone(phone):
        pattern = r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$'
        return re.match(pattern, phone) is not None
        
    
class WorkContact(Contact):
    def __init__(self, name, phone, updated_on, company):
        super().__init__(name, phone, updated_on)
        self.company = company

    def __str__(self):
        return super().__str__() + f" Компания: {self.company}"
    
work_contact = WorkContact("Иван Иванов", "7-123-456-78-90", datetime.now().isoformat(), "ООО Рога и Копыта")
contact = Contact("Петр Петров", "7-987-654-32-10", datetime.now().isoformat())
print(work_contact)
print(contact)