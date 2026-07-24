import re
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Contact {self.name}>"

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        pattern = r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$'
        return re.match(pattern, phone) is not None
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class PhoneBook:
    def add(self, name: str, phone: str, user_id):
        new_contact = Contact(
            name=name,
            phone=phone,
            updated_on=datetime.now().strftime("%d.%m.%Y %H:%M"),
            user_id=user_id)
        db.session.add(new_contact)
        db.session.commit()
    
    def delete(self, name: str, user_id) -> bool:
        contact = self.find(name, user_id)
        db.session.delete(contact)
        db.session.commit()
    
    def edit(self, name: str, new_phone: str, user_id) -> bool:
        contact = self.find(name, user_id)
        contact.phone = new_phone
        db.session.commit()
    
    def find(self, name: str, user_id):
        contact = Contact.query.filter_by(name=name, user_id=user_id).first()
        return contact
    
