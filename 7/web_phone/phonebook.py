import re
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.String(30))

    def __repr__(self):
        return f"<Contact {self.name}>"

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        pattern = r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$'
        return re.match(pattern, phone) is not None

class PhoneBook:
    def add(self, name: str, phone: str):
        new_contact = Contact(
            name=name,
            phone=phone,
            updated_on=datetime.now().strftime("%d.%m.%Y %H:%M"))
        db.session.add(new_contact)
        db.session.commit()
    
    def delete(self, name: str) -> bool:
        contact = self.find(name)
        db.session.delete(contact)
        db.session.commit()
    
    def edit(self, name: str, new_phone: str) -> bool:
        contact = self.find(name)
        contact.phone = new_phone
        db.session.commit()
    
    def find(self, name: str):
        contact = Contact.query.filter_by(name=name).first()
        return contact
    
