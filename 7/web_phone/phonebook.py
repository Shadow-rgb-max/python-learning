import re
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import MetaData

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contacts = db.relationship('Contact', backref='group', lazy=True)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(100))
    updated_on = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)

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
    def add(self, name: str, phone: str, company, user_id: int):
        new_contact = Contact(
            name=name,
            phone=phone,
            company=company,
            updated_on=datetime.now().strftime("%d.%m.%Y %H:%M"),
            user_id=user_id)
        db.session.add(new_contact)
        db.session.commit()
    
    def delete(self, name: str, user_id) -> bool:
        contact = self.find(name, user_id)
        db.session.delete(contact)
        db.session.commit()
    
    def edit(self, name: str, new_phone: str, new_company: str,user_id: int) -> bool:
        contact = self.find(name, user_id)
        contact.phone = new_phone
        contact.company = new_company
        db.session.commit()
    
    def find(self, name: str, user_id):
        contact = Contact.query.filter_by(name=name, user_id=user_id).first()
        return contact
    
